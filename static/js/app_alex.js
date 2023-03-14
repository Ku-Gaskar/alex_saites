
var ind=0;
function stopLine(){
    if (ind==0){
      // alert(document.getElementById('tyty').style.animationPlayState);
      document.querySelector('.newsticker span').style.setProperty("--speed_go","10s");
      document.querySelector('span#tyty').style.setProperty('animation-play-state','running');
      ind++;
    }
    else{
      if (ind==1){
        document.querySelector('span#tyty').style.setProperty('animation-play-state','paused');
       ind++;
      }
      else{
        document.querySelector('.newsticker span').style.setProperty("--speed_go","");
        ind=0;
      }
    }

};
