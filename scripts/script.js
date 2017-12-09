
/*JavaScript hamburger code taken from w3schools.com*/
function hamburgerToggle() { 
    var x = document.getElementById("myNavBar");
    if (x.className === "navBar") {
        x.className += " responsive";
    } else {
        x.className = "navBar";
    }
}



