var clickerNumber=0

function incrementation() {
    clickerNumber++;
    if(clickerNumber == 5) {
        $('#h2counter').text("https://www.youtube.com/watch?v=ylbmc1hAofg");
    }
    else{
     $('#h2counter').text('count: ' + clickerNumber);
    }
}