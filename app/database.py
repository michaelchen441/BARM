"""Defines all the functions related to the database"""
from app import db



#Generation of user Id
def how_many_users_exist() -> int:
    conn = db.connect()
    query = 'Select COUNT(*) from UserInfo'
    query_results = conn.execute(query).fetchall()
    for results in query_results:
        return results[0]

#Checks if user exists
def does_user_exist(userName) -> bool:
    # return("Something")
    conn = db.connect()
    query = "Select COUNT(*) from UserInfo where userName = '"+userName+"';"
    query_results = conn.execute(query).fetchall()
    conn.close()
    return((query_results[0][0] != 0))
#
def createUser(userName:str, password: str) ->  bool:
    if not (does_user_exist(userName)):
        userid = how_many_users_exist() +1
        conn = db.connect()
        query = 'Insert Into UserInfo VALUES ({},"{}","{}");'.format(
            userid, userName,password)
        conn.execute(query)
        conn.close()
        return True
    else:
        return False
#
# #Updates Password if user exists
def updatePassword(userName:str, new_password: str) ->  bool:
    if(does_user_exist(userName)):
        conn = db.connect()
        query = 'Update UserInfo set password = "{}" where userName = "{}"'.format(new_password,userName)
        conn.execute(query)
        conn.close()
        return True
    else:
        return False
#
def addLikeArtist(userid:int, artistName: str) ->  bool:
    if not(does_user_already_like_artist(userid,artistName)):
        artistId = findArtistIDbyName(artistName)
        conn = db.connect()
        query = 'Insert Into ArtistsUsersLike VALUES ({}, "{}");'.format(
            userid, artistId)
        conn.execute(query)
        conn.close()
        return True
    else:
        return False
#
def removeLikeArtist(userid:int, artistName: str) ->  bool:

    if(does_user_already_like_artist(userid,artistName)):
        artistId = findArtistIDbyName(artistName)
        conn = db.connect()
        query = 'Delete from ArtistsUsersLike WHERE userId ={} and artistId ="{}"'.format(
            userid, artistId)
        conn.execute(query)
        conn.close()
        return True
    else:
        return False
#
def findArtistIDbyName( artistName: str) -> str:
    conn = db.connect()
    query_results = conn.execute('Select * from Artists WHERE name = "{}";'.format(artistName)).fetchall()
    conn.close()
    artist = {}
    return query_results[0][0]
#
#
def does_user_already_like_artist(userid:int, artistName: str) -> bool:

    artistId = findArtistIDbyName(artistName)
    conn = db.connect()
    query_results = conn.execute("Select COUNT(*) from ArtistsUsersLike WHERE userId = {} AND artistId = '{}' ;".format(userid, artistId)).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        if result[0] == 0:
            return False
        else:
            return True

#
def showLikedArtist(userid)-> dict:
    conn = db.connect()
    query_results = conn.execute("Select Artists.name from ArtistsUsersLike NATURAL JOIN  Artists WHERE userId = {};".format(userid)).fetchall()
    conn.close()
    artist_list = []
    for result in query_results:
        artist_list.append(result[0])
    return artist_list
#
#second advanced query
def suggestPlaylist(userid)-> dict:
    conn = db.connect()

    likedArtists = showLikedArtist(userid)
    if not likedArtists:
        return {}
    insert = ""
    for artist in likedArtists:
        insert = insert + "a.name = '" + artist + "' OR "
    insert = insert[:-4]

    query = "SELECT p.name, COUNT(*) numMatches FROM SongsInAllPlaylists sp  NATURAL JOIN Songs s JOIN AllPlaylists p on sp.playlistId = p.playlistId JOIN Artists a on s.artistId = a.artistId WHERE {} GROUP BY sp.playlistId ORDER BY numMatches DESC LIMIT 3".format(insert)

    query_results = conn.execute(query).fetchall()
    conn.close()
    artist_list = []
    for result in query_results:
        artist_list.append(result[0])
    return artist_list
#
#first advanced query
def songsByTwoArtists(artist1, artist2)-> dict:
    conn = db.connect()

    query = "SELECT s.name, a.name FROM Songs s JOIN Artists a ON s.ArtistId =a.ArtistId WHERE a.name = '{}' UNION SELECT s2.name, a2.name FROM Songs s2 JOIN Artists a2 ON s2.ArtistId = a2.ArtistId WHERE a2.name = '{}'".format(artist1,artist2)

    query_results = conn.execute(query).fetchall()
    conn.close()
    song_list = []
    for result in query_results:
        song_list.append(result[0])
    return song_list

# # /////////
