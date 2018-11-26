var clickerNumber=0
var controller=1

function incrementation() {
    if(controller==1) {
        clickerNumber++;
        $('#h2counter').text('total: ' + clickerNumber);
        if(clickerNumber == 5) {
            $('#pressHref').text("PRESS");
            document.getElementById("pressHref").href="https://www.youtube.com/watch?v=ylbmc1hAofg";
            //$('#h2counter').text('');
            controller = 0;
        }
    }
}

function collapse() {
    if(document.getElementById("mynavbar").aria-expanded == "false") {
        //document.getElementById("mynavbar").class="navbar-collapse collapse in";
        //document.getElementById("mynavbar").aria-expanded="true";
        $('#mynavbar').class="navbar-collapse collapse in";
        $('#mynavbar').aria-expanded="true";
    }
    else {
        //document.getElementById("mynavbar").class="navbar-collapse collapse";
        //document.getElementById("mynavbar").aria-expanded="false";
        $('#mynavbar').class="navbar-collapse collapse";
        $('#mynavbar').aria-expanded="false";
    }
}