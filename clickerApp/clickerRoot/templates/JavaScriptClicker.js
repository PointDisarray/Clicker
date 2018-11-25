var clicksNumber=0

function incrementation() {

    clickerNumber++
    if(clickerNumber== 5) {
        var element = getElementById('h2counter')
        element.textContent = 'https://www.youtube.com/watch?v=ylbmc1hAofg'
        console.log('inside if'+clickerNumber)
    }
    var element = getElementById('h2counter')
        element.textContent = 'Shit'
        console.log('outside if'+clickerNumber)
}