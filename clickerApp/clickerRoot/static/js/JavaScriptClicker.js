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

function newUser () {
    if (document.getElementById("button1").style.display == 'none') {
        document.getElementById("button1").style.display == 'block'
        document.getElementById("nickname").style.display == 'none'
    }

}