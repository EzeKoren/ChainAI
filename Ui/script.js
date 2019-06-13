$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        M.AutoInit();
        handle_input("getfile", 0, 0);
        $('#c00').click(function() {
            console.log(jsonfile);
            placedot(1);
        });
    });
});
var jsonfile;
var url = "http://127.0.0.1:5000/input";

function handle_input(req, cord, player) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    var data = new FormData();
    data.append("request", req);
    data.append("cord", cord);
    data.append("player", player);
    xhr.send(data);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            //var jsonobj = JSON.parse(xhr.responseText);
            console.log(xhr.responseType);
            jsonfile = (xhr.responseText);
        }
    };
}

function placedot(id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var jsonobj = JSON.parse(this.responseText);
            document.getElementById("demo").innerHTML = myObj.name;
        }
    };
    xmlhttp.open("GET", jsonfile, true);
    xmlhttp.send(file);
    console.log(jsonobj)
}