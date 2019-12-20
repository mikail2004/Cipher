function darpa() {
	var text = document.getElementById("text").value
	eel.to_morse_code(text);
}

eel.expose(proto)

function proto(message){
    const enc = document.getElementById("answer")
    enc.innerHTML = message
}