var tablero;
$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        M.AutoInit();
        $('#c00').click(function() {
            handle_input(34, "hola")
        });
    });
});

var url = "http://127.0.0.1:5000/input";

function handle_input(cord, player) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    var data = new FormData();
    data.append("cord", cord)
    data.append("player", player)
    xhr.send(data);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(xhr.responseText);
        }
    };
}