
function oncl() {
    var div = document.getElementsByClassName('header_menu_burger');
    style = div[0].style;
    if (style.top != "60px") {
        style.top = "60px";
    } else {
        style.top = "-100px";
    }
};
