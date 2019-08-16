// ----------------------------- //

var url = "http://localhost:5000/";

// ---------------------------- //

$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        M.AutoInit();
        makefile();
        $("a.btn").click(async function() {
            if (working == false) {
                working = true;
                var cord = $(this).attr('id');
                console.log(cord);
                placedot(cord, player);
            }
        });
    });
});
var colorempty1 = "grey";
var colorempty2 = "lighten-2";
var color11 = "red";
var color12 = "accent-2";
var color21 = "green";
var color22 = "darken-2";
var working = false;
var player;
var error;
var jsonobj;
var p1;
var p2;
var step;

function makefile() {
    working = true
    player = 1
    var xhr = new XMLHttpRequest();
    var dir = url + "create";
    xhr.open("POST", dir, true);
    xhr.send(null);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            jsonobj = JSON.parse(xhr.responseText);
            oldobj = jsonobj;
            displayboard();
            console.log(jsonobj);
        }
    };
}

function placedot(cord, player, callback) {
    M.Toast.dismissAll();
    var xhr = new XMLHttpRequest();
    var dir = url + "input";
    xhr.open("POST", dir, true);
    var data = new FormData();
    data.append("cord", cord);
    data.append("player", player);
    xhr.send(data);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            if (xhr.responseText == "failed") {
                error = true;
            } else if (xhr.responseText == "won") {
                M.toast({ html: 'Gano el ' + player });
                makefile();
            } else {
                error = false;
                oldobj = jsonobj;
                console.log(xhr.responseText);
                // TODO: recibir si alguien gano, al mismo tiempo que recibe el tablero
                jsonobj = JSON.parse(xhr.responseText);
                step = String(cord);
                console.log(oldobj);
                console.log(step);
                console.log(jsonobj);
                console.log(error);
                changeplayer();
            };
        }
    };
}



function changeplayer() {
    if (error == false) {
        console.log(player);
        if (player == 1) {
            player = 2;
        } else if (player == 2) { player = 1; }
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
    while (key < Object.keys(jsonobj.boxes).length) {
        // console.log("display keyboard: " + Object(jsonobj.boxes[key].id));
        var div = document.getElementById(Object(jsonobj.boxes[key].cord));
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
    // if (turncount > 1) {
    //     if (p1 == 0) {
    //         M.toast({ html: 'Gano el 2' });
    //         sendtoai(2);
    //         makefile();
    //     }
    //     if (p2 == 0) {
    //         M.toast({ html: 'Gano el 1' });
    //         turncount = 0;
    //         makefile();
    //     }
    // }
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