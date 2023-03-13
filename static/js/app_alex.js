
var ind=1;
function stopLine(){
    if (ind==1){
      document.querySelector('.newsticker span').style.setProperty("--speed_go","10s");
      ind=0;
    }
    else{
      document.querySelector('.newsticker span').style.setProperty("--speed_go","");
      ind=1;
    }
};
