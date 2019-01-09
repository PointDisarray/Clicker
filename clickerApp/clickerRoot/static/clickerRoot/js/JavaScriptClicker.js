var clickerNumber
var global_counter
var controller=1

//function incrementation(videoId, username, csrf_token) {
//    if(controller==1) {
//        clickerNumber++;
//        $('#h2counter').text('total: ' + clickerNumber);
//        global_counter++;
//        $(".Gcount").text('Global count: '+ (global_counter));
//        if(clickerNumber % 25 == 0) {
//            $("#videoDiv").show();
//            $("#button1").hide();
//            controller = 0;
//        }
//        $.ajax({
//            url: "/incrementation",
//            type: "POST",
//            data: {csrfmiddlewaretoken:  JSON.stringify(csrf_token),'username' : username, 'clickerNumber' : clickerNumber},
//            "Content-type": "application/json",
//            dataType: 'json',
//            success: function(data){
//                console.log(data);
//            },
//            failure: function(errMsg) {
//                alert(errMsg);
//            },
//        });
//    }
//};

//function refresh() {
//  $.ajax({
//  url: 'global_getter',
//  success: function(data) {
//    $(".Gcount").text('Global count: ' + data['counter__sum']);
//    global_counter = data['counter__sum'];
//  }
// });
//};

//$(document).ready(function ($) {
//  refresh();
//  var int = setInterval("refresh()", 3000);
//});

function newUser () {
        $("#button1").show();
        $("#nickname").hide();
}

function videoSearch(videoTag) {
        $.ajax({
            url: "/videoSearch",
            type: "POST",
            data: {'videoTag' : videoTag},
            "Content-type": "application/json",
            dataType: 'json',
            success: function(data){
                console.log(data["videoId"]);
                $("iframe").attr('src', "https://www.youtube.com/embed/"+data["videoId"]+"?autoplay=1&controls=0");
            },
            failure: function(errMsg) {
                alert(errMsg);
            },
        });

}
/*function hideCollapse() {
    $('.navbar').hideCollapse;
}*/

function onLoader(counter){
    clickerNumber = counter;
}