var tablero;
$(window).on("load", function() {
    $(document).ready(function() {
        console.log("ready!");
        M.AutoInit();
        $('#c00').click(function() {
            M.toast({ html: 'Hello, world' })
            $.ajax({
                type: "POST",
                url: "../Python/testfile.py",
                data: { param: "text" }
            }).done(function(o) {
                M.toast({ html: 'done' })
            });
            // MAS CODIGO ACA
        });
    });
});