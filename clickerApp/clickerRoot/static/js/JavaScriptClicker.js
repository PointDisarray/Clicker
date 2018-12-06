var clickerNumber=0
var controller=1

function incrementation(videoId) {
    if(controller==1) {
        clickerNumber++;
        $('#h2counter').text('total: ' + clickerNumber);
        if(clickerNumber == 5) {
            $("#videoDiv").show();
            $("#button1").hide();
            controller = 0;
        }
    }
}

function newUser () {
        $("#button1").show();
        $("#nickname").hide();
}