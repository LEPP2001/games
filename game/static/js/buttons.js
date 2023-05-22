function showGato() {   
    if(document.getElementById('gato-game').style.display == 'block') {
        document.getElementById('gato-game').style.display = 'none';
    }
    else {
        document.getElementById('pong-game').style.display = 'none';
        document.getElementById('gato-game').style.display = 'block';
    }
}
  
function showPong() {
    if(document.getElementById('pong-game').style.display == 'block') {
        document.getElementById('pong-game').style.display = 'none';
    }
    else {
        document.getElementById('pong-game').style.display = 'block';
        document.getElementById('gato-game').style.display = 'none';
    }
}
  