function postMessage()
{
    var chat10 = document.getElementById("chat").value;
    chat10.innerHTML = "Posting . . .";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            
            var chat10 = document.getElementById("chat").value;
            chat1.innerHTML = this.responseText["chat10"]+chat10;

        }
    };
    xhttp.open("POST", "/forumResults", true);
    xhttp.send();
}

