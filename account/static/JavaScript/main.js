
function oncl() {
    var div = document.getElementsByClassName('header_menu_burger');
    style = div[0].style;
    if (style.top != "60px") {
        style.top = "60px";
    } else {
        style.top = "-100px";
    }
};

function mobileoncl() {
    var div = document.getElementsByClassName('mobile_header_menu_burger');
    style = div[0].style;
    if (style.left != "0px") {
        style.left = "0px";
    } else {
        style.left = "-1000px";
    }
};
