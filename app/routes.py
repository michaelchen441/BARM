""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

# @app.route("/delete/<int:task_id>", methods=['POST'])
# def delete(task_id):
#     """ recieved post requests for entry delete """
#
#     try:
#         db_helper.remove_task_by_id(task_id)
#         result = {'success': True, 'response': 'Removed task'}
#     except:
#         result = {'success': False, 'response': 'Something went wrong'}
#
#     return jsonify(result)
#
#
# @app.route("/edit/<int:task_id>", methods=['POST'])
# def update(task_id):
#     """ recieved post requests for entry updates """
#
#     data = request.get_json()
#
#     try:
#         if "status" in data:
#             db_helper.update_status_entry(task_id, data["status"])
#             result = {'success': True, 'response': 'Status Updated'}
#         elif "description" in data:
#             db_helper.update_task_entry(task_id, data["description"])
#             result = {'success': True, 'response': 'Task Updated'}



@app.route("/remove_artist", methods=['POST'])
def remove_artist():
    data = request.get_json()
    success= db_helper.removeLikeArtist(data['userId'],data['artistName'])
    result = {'success': True, 'response': success}
    return jsonify(result)


@app.route("/add_artist", methods=['POST'])
def add_artist():
    data = request.get_json()
    success= db_helper.addLikeArtist(data['userId'],data['artistName'])
    result = {'success': True, 'response': success}
    return jsonify(result)

@app.route("/create_user", methods=['POST'])
def create():
    data = request.get_json()
    success= db_helper.createUser(data['userName'],data['password'])
    result = {'success': True, 'response': success}
    return jsonify(result)

@app.route("/update_password", methods=['POST'])
def update():
    data = request.get_json()
    success= db_helper.updatePassword(data['userName'],data['password'])
    result = {'success': True, 'response': success}
    return jsonify(result)

@app.route("/")
def homepage():
    likedArtists = db_helper.showLikedArtist(1001)
    suggestPlaylist = db_helper.suggestPlaylist(1001)
    return render_template("index.html",artists =likedArtists,playlist= suggestPlaylist)
