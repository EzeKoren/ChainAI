$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        player = 1
        M.AutoInit();
        makefile(1);
        $("a.btn").click(async function() {
            if (working == false) {
                var id = $(this).attr('id');
                console.log(id);
                placedot(jsonfile, id, player);
            }
        });
    });
});
var working = false;
var player;
var jsonfile;
var jsonobj;
var url = "http://127.0.0.1:5000/";

function makefile(dou, callback) {
    working = true
    var xhr = new XMLHttpRequest();
    var dir = url + "create";
    xhr.open("POST", dir, true);
    xhr.send(null);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
            jsonfile = (xhr.responseText);
            working = false
        }
    };
}

async function placedot(file, cord, player, callback) {
    working = true
    var xhr = new XMLHttpRequest();
    var dir = url + "input";
    xhr.open("POST", dir, true);
    var data = new FormData();
    data.append("file", file);
    data.append("cord", cord);
    data.append("player", player);
    xhr.send(data);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            jsonobj = JSON.parse(xhr.responseText);
            console.log(jsonobj);
            changeplayer()
        }
    };
}

function changeplayer() {
    if (jsonobj != "failed") {
        console.log(player);
        if (player == 1) { player = 2; } else if (player == 2) { player = 1; }
    } else M.toast({ html: 'That place is occupied' });
}

function displayboard() {
    Object.keys(jsonobj)
    working = false
}