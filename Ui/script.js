$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        M.AutoInit();
        makefile();
        $("a.btn").click(async function() {
            if (working == false) {
                working = true;
                var id = $(this).attr('id');
                console.log(id);
                placedot(jsonfile, id, player);
            }
        });
    });
});
var turncount = 0;
var colorempty1 = "grey";
var colorempty2 = "lighten-2";
var color11 = "red";
var color12 = "accent-2";
var color21 = "green";
var color22 = "darken-2";
var working = false;
var player;
var error;
var jsonfile;
var jsonobj;
var obserb1 = [];
var obserb2 = [];
var url = "http://localhost:5000/";
var p1;
var p2;
var step;

function makefile() {
    working = true
    player = 1
    obserb1 = [];
    obserb2 = [];
    var xhr = new XMLHttpRequest();
    var dir = url + "create";
    xhr.open("POST", dir, true);
    xhr.send(null);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
            jsonobj = JSON.parse(xhr.responseText);
            oldobj = jsonobj;
            displayboard();
            console.log(jsonfile);
            console.log(jsonobj);
        }
    };
}

function placedot(file, cord, player, callback) {
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
                oldobj = jsonobj;
                jsonobj = JSON.parse(xhr.responseText);
                step = String(cord);
                console.log(oldobj);
                console.log(step);
                console.log(jsonobj);
                appenddata(player);
            };
            console.log(error);
            changeplayer();
        }
    };
}

function appenddata(pl) {
    if (pl == 1) {
        preadd = [JSON.stringify(oldobj), step]
        obserb1.push(preadd);
        console.log(obserb1);
    } else if (pl == 2) {
        preadd = [JSON.stringify(oldobj), step]
        obserb2.push(preadd);
        console.log(obserb2);
    }
}

function changeplayer() {
    if (error == false) {
        console.log(player);
        if (player == 1) {
            player = 2;
            turncount++;
        } else if (player == 2) { player = 1; }
        console.log("turno " + turncount);
        M.Toast.dismissAll();
        displayboard();
    } else {
        M.Toast.dismissAll();
        M.toast({ html: 'Está ocupado el lugar' });
        working = false;
    }
}

function displayboard() {
    var key = 0;
    p1 = 0;
    p2 = 0;
    while (key < Object.keys(jsonobj.boxes).length) {
        // console.log("display keyboard: " + Object(jsonobj.boxes[key].id));
        var div = document.getElementById(Object(jsonobj.boxes[key].id));
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
        changecolor(div, Number(Object(jsonobj.boxes[key].player)), true)
        key++;
    }
    if (turncount > 1) {
        if (p1 == 0) {
            M.toast({ html: 'Gano el 2' });
            turncount = 0;
            sendtoai(2);
            makefile();
        }
        if (p2 == 0) {
            M.toast({ html: 'Gano el 1' });
            turncount = 0;
            sendtoai(1);
            makefile();
        }
    }
    changecolor(document.getElementById("titlebar"), player, false);
    working = false;
}

function changecolor(div, player, counting) {
    switch (player) {
        case 1:
            if (div.classList.contains(colorempty1)) {
                div.classList.remove(colorempty1);
                div.classList.remove(colorempty2);
                div.classList.add(color11);
                div.classList.add(color12);
            }
            if (div.classList.contains(color21)) {
                div.classList.remove(color21);
                div.classList.remove(color22);
                div.classList.add(color11);
                div.classList.add(color12);
            }
            p1++;
            break;
        case 2:
            if (div.classList.contains(colorempty1)) {
                div.classList.remove(colorempty1);
                div.classList.remove(colorempty2);
                div.classList.add(color21);
                div.classList.add(color22);
            }
            if (div.classList.contains(color11)) {
                div.classList.remove(color11);
                div.classList.remove(color12);
                div.classList.add(color21);
                div.classList.add(color22);
            }
            p2++;
            break;
        default:
            if (div.classList.contains(color11)) {
                div.classList.remove(color11);
                div.classList.remove(color12);
                div.classList.add(colorempty1);
                div.classList.add(colorempty2);
            }
            if (div.classList.contains(color21)) {
                div.classList.remove(color21);
                div.classList.remove(color22);
                div.classList.add(colorempty1);
                div.classList.add(colorempty2);
            }
    }
}

// function sendtoai(player) {
//     if (player == 1) {
//         console.log(obserb1);
//         var xhr = new XMLHttpRequest();
//         var dir = url + "appenddata";
//         xhr.open("POST", dir, true);
//         var data = new FormData();
//         data.append("player", 1);
//         data.append("data", obserb1);
//         xhr.send(data);
//     }
//     if (player == 2) {
//         console.log(obserb2);
//         var xhr = new XMLHttpRequest();
//         var dir = url + "appenddata";
//         xhr.open("POST", dir, true);
//         var data = new FormData();
//         data.append("player", 2);
//         data.append("data", obserb2);
//         xhr.send(data);
//     }
// }