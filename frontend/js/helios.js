const box =
document.getElementById("msg");

const chat =
document.getElementById("chat");

document
.getElementById("sendBtn")
.addEventListener(
"click",
sendMessage
);

box.addEventListener(
"keydown",
e=>{
if(e.key==="Enter")
sendMessage();
}
);

async function sendMessage(){

let msg =
box.value.trim();

if(!msg) return;

chat.innerHTML +=
`<div class="user">
HC > ${msg}
</div>`;

box.value="";

chat.innerHTML +=
`<div
class="helios"
id="thinking">
HELIOS is thinking...
</div>`;

chat.scrollTop =
chat.scrollHeight;

try{

let response =
await fetch(
"https://helios-gpvn.onrender.com",
{
method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({
message:msg
})

}
);

let data =
await response.json();

document
.getElementById(
"thinking"
)
.remove();

chat.innerHTML +=
`<div class="helios">
HELIOS > ${data.response}
</div>`;

chat.scrollTop =
chat.scrollHeight;



}

catch(err){

let t =
document.getElementById(
"thinking"
);

if(t) t.remove();

chat.innerHTML +=
`<div class="helios">
ERROR:
Connection Failed
</div>`;

}

}
