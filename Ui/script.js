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
var colorempty = "#e0e0e0"
var color1 = "#ff5252"
var color2 = "#388e3c"
var working = false;
var player;
var error;
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

function placedot(file, cord, player, callback) {
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
            if (xhr.responseText == "failed") { error = true } else {
                error = false;
                jsonobj = JSON.parse(xhr.responseText);
                console.log(jsonobj);
            };
            console.log(error)
            changeplayer();
        }
    };
}

let changeplayer = () => {
    if (error == false) {
        console.log(player);
        if (player == 1) { player = 2; } else if (player == 2) { player = 1; }
        M.Toast.dismissAll();
        displayboard();
    } else {
        M.Toast.dismissAll();
        M.toast({ html: 'Está ocupado el lugar' });
        working = false;
    }
}

let displayboard = () => {
    let key = 0;
    while (key < Object.keys(jsonobj.boxes).length) {
        // console.log("display keyboard: " + Object(jsonobj.boxes[key].id));
        let div = document.getElementById(Object(jsonobj.boxes[key].id));
        var points = Number(Object(jsonobj.boxes[key].points));
        console.log(points);
        if (points == 1) {

            div.innerHTML = "<img class = 'icon' src = './icon/1.png'>";
        }
        if (points == 2) {
            div.innerHTML = "<img class = 'icon' src = './icon/2.png'>";
        }
        if (points == 3) {
            div.innerHTML = "<img class = 'icon' src = './icon/3.png'>";
        }
        if (points == 0) {
            div.innerHTML = "<img class = 'icon' src = './icon/0.png'>";
        }
        key++;
    }
    working = false;
}