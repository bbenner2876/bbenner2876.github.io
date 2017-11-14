
function hamburgerToggle() { /*JavaScript hamburger code taken from w3schools.com*/
    var x = document.getElementById("myNavBar");
    if (x.className === "navBar") {
        x.className += " responsive";
    } else {
        x.className = "navBar";
    }
}

function popUp(){
    alert("Popped up!");
}
