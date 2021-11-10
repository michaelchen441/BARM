console.log("hello");
function add(){
  alert("Artist added!!");
}
function deletes(){
  alert("Artist deleted!!");
}
$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal



    $('#sign-up').click(function () {
        console.log("signedup");
        const userName = $('#uname').val()
        const password = $('#password').val()
        console.log(userName,password);
        // console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: '/create_user',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userName': userName,
                'password': password
            }),
            success: function (res) {
                if (res.response) {
                  alert("new user created")
                }
                else {
                  alert("user already taken")
                }

            },
            error: function () {

                console.log('Error');
            }
        });
    });

    $('#update-pwd').click(function () {

        const userName = $('#uname').val()
        const password = $('#password').val()
        console.log(userName,password);
        // console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: '/update_password',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userName': userName,
                'password': password
            }),
            success: function (res) {
                if (res.response) {
                  alert("password updated")
                }
                else {
                  alert("user doesnt exists")
                }

            },
            error: function () {

                console.log('Error');
            }
        });
    });

    $('#add-artist').click(function () {

        const artistName = $('#add1').val()
        console.log(artistName);
        $.ajax({
            type: 'POST',
            url: '/add_artist',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userId': 1001,
                'artistName': artistName
            }),
            success: function (res) {
                if (res.response) {
                  alert("artist added")
                  location.reload()

                }
                else {
                  alert("artist already exists")
                }

            },
            error: function () {

                console.log('Error');
            }
        });
    });

    $('#remove-artist').click(function () {

        const artistName = $('#ArtistDeleteBox').val()
        console.log(artistName);
        $.ajax({
            type: 'POST',
            url: '/remove_artist',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userId': 1001,
                'artistName': artistName
            }),
            success: function (res) {
                if (res.response) {
                  alert("artist deleted")
                  location.reload()
                }
                else {
                  alert("artist doesnt exists")
                }

            },
            error: function () {
                console.log('Error');
            }
        });
    });





    });
