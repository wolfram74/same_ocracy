console.log('javascript loaded')
window.onload = listenerSetup

function listenerSetup(){
  console.log('setup')
  var choices = document.getElementsByTagName('a')
  for(var index=0; index < choices.length; index++){
    choices[index].addEventListener('click', answerHandler)
  }

}

function answerHandler(event){
  event.preventDefault()
  var flasher = document.getElementsByClassName('comparison')[0]
  if(event.target.className === 'correct'){
    flasher.style.backgroundColor = 'rgb(200,240,200)'
  } else{
    flasher.style.backgroundColor = 'rgb(240,200,200)'
  }
  setTimeout(function(){location.reload()}, 500) // shitty solution?
  // setTimeout(function(){event.target.dispatchEvent(event)}, 100) // better solution?
}

