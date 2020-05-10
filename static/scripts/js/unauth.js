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
place(f, 10, 10, "https://lh3.googleusercontent.com/proxy/6dwpJLuOHxw9x5yEY8GwZSq_veXnco3woM8eIVs94ik9ZDFcf-THQOFM6mkgHMctWH_HRFLDDwsUeg-H4ShkmKD9A1v1KLKpxpnnctEgnJzIUY4");
await new Promise(r => setTimeout(r, 2000));
place(u, 70, 10, "https://lh3.googleusercontent.com/proxy/ggkFyRamtD60PZfrFkNXv160gBAJt-9twQmrBFUKvcVO-Zp8xeJkWcJ8nrJ4ta4cyCHOSzxHuuSvpnKVnXZYQb0E8hck9kAAe5mF_zTIoTnBvoE7Gek2e_JkQA");
await new Promise(r => setTimeout(r, 2000));
place(k, 120, 10, "http://assets.stickpng.com/images/5a01bb577ca233f48ba627b9.png");
await new Promise(r => setTimeout(r, 2000));
place(y, 70, 70, "https://i.dlpng.com/static/png/1585721-letter-y-png-download-image-y-png-628_800_preview.png");
await new Promise(r => setTimeout(r, 2000));
place(o, 70, 70, "https://toppng.com/uploads/preview/capital-letter-o-11552740101fhmfngpaay.png");
await new Promise(r => setTimeout(r, 2000));
place(u2, 70, 70, "https://lh3.googleusercontent.com/proxy/ggkFyRamtD60PZfrFkNXv160gBAJt-9twQmrBFUKvcVO-Zp8xeJkWcJ8nrJ4ta4cyCHOSzxHuuSvpnKVnXZYQb0E8hck9kAAe5mF_zTIoTnBvoE7Gek2e_JkQA");
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
