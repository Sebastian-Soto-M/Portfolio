'use strict';
//Get the button:
let mybutton = $("#btn_scroll_top");

$(function () {
    const offset = 20; //Offset of 20px
    $('#nv_technologies').click(function (e) {
        $('html, body').animate({
            scrollTop: $("#technologies").offset().top + offset
        }, 1500);

    });
    mybutton.click(function (e) {
        $('html, body').animate({
            scrollTop: $("#top").offset().top
        }, 1500);
        mybutton.fadeOut("slow","linear");
    });
});



// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        mybutton.fadeIn("slow","linear");
    } else {
        mybutton.fadeOut("slow","linear");
    }
}