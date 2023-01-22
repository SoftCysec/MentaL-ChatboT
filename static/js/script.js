function submitChat() {
    // Get the user's input
    var text = document.getElementById("textinput").value;

    // Clear the textarea
    document.getElementById("textinput").value = "";

    // Send a POST request to the server with the user's input
    // and display the chatbot's response in the chatlogs div
    fetch("/", {
            method: "POST",
            body: JSON.stringify({ text: text }),
            headers: { "Content-Type": "application/json" }
        })
        .then(res => res.text())
        .then(data => {
            var chatlogs = document.getElementById("chatlogs");
            chatlogs.innerHTML += "<div class='chatbot'>" + data + "</div>";
            chatlogs.scrollTop = chatlogs.scrollHeight;
        });
}