var clickerNumber
var controller=1

function incrementation(videoId, username, csrf_token) {
    if(controller==1) {
        clickerNumber++;
        $.ajax({
            url: "/incrementation",
            type: "POST",
            data: {csrfmiddlewaretoken:  JSON.stringify(csrf_token),'username' : username, 'clickerNumber' : clickerNumber},
            "Content-type": "application/json",
            dataType: 'json',
            success: function(data){
                $(".Gcount").text('Global count: ' + data['counter__sum']);
            },
            failure: function(errMsg) {
                alert(errMsg);
            },
        });
        $('#h2counter').text('total: ' + clickerNumber);
        if(clickerNumber % 25 == 0) {
            $("#videoDiv").show();
            $("#button1").hide();
            controller = 0;
        }
    }
}

function incrementation(videoId, username, csrf_token) {
    if(controller==1) {
        clickerNumber++;
        $.ajax({
            url: "/incrementation",
            type: "POST",
            data: {csrfmiddlewaretoken:  JSON.stringify(csrf_token),'username' : username, 'clickerNumber' : clickerNumber},
            "Content-type": "application/json",
            dataType: 'json',
            success: function(data){
                console.log(data);
            },
            failure: function(errMsg) {
                alert(errMsg);
            },
        });
        $('#h2counter').text('total: ' + clickerNumber);
        if(clickerNumber % 25 == 0) {
            $("#videoDiv").show();
            $("#button1").hide();
            controller = 0;
        }
    }
};

function refresh() {
  $.ajax({
  url: 'global_getter',
  success: function(data) {
    $(".Gcount").text('Global count: ' + data['counter__sum']);
  }
 });
};


$(document).ready(function ($) {
  refresh();
  var int = setInterval("refresh()", 5000);
});

function newUser () {
        $("#button1").show();
        $("#nickname").hide();
}

function onLoader(counter){
    clickerNumber = counter;
}