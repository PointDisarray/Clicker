var clickerNumber
var global_counter
var controller=1

function incrementation(videoId, username, csrf_token) {
    if(controller==1) {
        clickerNumber++;
        $('#h2counter').text('total: ' + clickerNumber);
        global_counter++;
        $(".Gcount").text('Global count: '+ (global_counter));
        if(clickerNumber % 25 == 0) {
            $("#videoDiv").show();
            $("#button1").hide();
            controller = 0;
        }
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
    }
};

function refresh() {
  $.ajax({
  url: 'global_getter',
  success: function(data) {
    $(".Gcount").text('Global count: ' + data['counter__sum']);
    global_counter = data['counter__sum'];
  }
 });
};

function send_ready() {
  $.ajax({
  url: 'init_socket',
  success: function(data) {
    console.log("socket start: " + data['socket start']);
  }
 });
};


$(document).ready(function ($) {
//  refresh();
//  var int = setInterval("refresh()", 3000);

var connection = new WebSocket('ws://djangoclickers.herokuapp.com:9005');

send_ready();

connection.onmessage = function (e) {
  console.log('Server: ' + e.data);
};
});

function newUser () {
        $("#button1").show();
        $("#nickname").hide();
}

function onLoader(counter){
    clickerNumber = counter;
}