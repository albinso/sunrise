// document.getElementById("dis").disabled = true;
var counter = 0;
//var x = document.getElementById("myDIV");
var myLayer = document.getElementById("parent");
myLayer.style.position = 'absolute';
myLayer.style.left = '10px';
myLayer.style.top = '10px';
myLayer.style.width = '1200px';
myLayer.style.height = '800px';
myLayer.style.padding = '10px';
document.body.appendChild(myLayer);
var f = document.createElement("img");
var u = document.createElement("img");
var k = document.createElement("img");
var y = document.createElement("img");
var o = document.createElement("img");
var u2 = document.createElement("img");

function place(element, x, y, src) {
	  //document.getElementById("dis").disabled = false;
	  counter++;
	  element.style.marginLeft = x + "px";
	  element.style.marginTop = y + "px";
	  element.style.width = "120px";
	  element.style.height = "120px";
	  element.setAttribute("src", src);
	  document.getElementById("parent").appendChild(element);
}
async function doStuff() {
place(f, 10, 10, "/static/img/f.png");
await new Promise(r => setTimeout(r, 2000));
place(u, 70, 10, "/static/img/u.png");
await new Promise(r => setTimeout(r, 2000));
place(k, 70, 10, "/static/img/k.png");
await new Promise(r => setTimeout(r, 2000));
place(y, 70, 10, "/static/img/y.png");
await new Promise(r => setTimeout(r, 2000));
place(o, 70, 10, "/static/img/o.png");
await new Promise(r => setTimeout(r, 2000));
place(u2, 70, 10, "/static/img/u.png");
}
var count = 1;
var audio = new Audio('/static/audio/fuku.wav');
audio.addEventListener('ended', function(){
	   this.currentTime = 0;
	   if(count <= 3){
		         this.play();
		      }
	   count++;
}, false);
audio.play();
doStuff();
