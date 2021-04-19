document.getElementById("texttt").style.color = "white";

var github_logo_filter = document.getElementById("github").style.filter;
var right_division_bg = document.getElementById("right").style.backgroundColor;
var left_division_bg = document.getElementById("left").style.backgroundColor;
var Above_text_writer_text_shadow = document.getElementById("texttt").style.textShadow;
var Above_text_writer_text_color = document.getElementById("texttt").style.color;
var The_typewriter_text_color = document.getElementById("typed").style.color;
var tablink$ = document.getElementsByClassName("tablink");
var p_tag_color = document.querySelector("p").style.color;
var form_div_bg = document.getElementById("form-div").style.backgroundColor;
var form_of_contact = document.getElementById("form1").style.backgroundColor;
var chatform_background_color = document.getElementsByClassName("form")[0].style.backgroundColor;
var chatform_border = document.getElementsByClassName("form")[0].style.border;
var chat_input_box_background_color = document.getElementsByClassName("chat_input")[0].style.backgroundColor;
var chat_input_borderbottom = document.getElementsByClassName("chat_input")[0].style.borderBottom;
var send_button_font_color = document.getElementById("sendButton").style.color;
var send_button_background_color = document.getElementById("sendButton").style.backgroundColor;
var src_of_github_readme_stats = document.getElementById("stats").src
var src_of_github_langs = document.getElementById("langs").src

var dark = false

function changer() {
    if (dark == true) {
        darker()
        dark = false
        document.getElementById("toggle-btn").innerHTML = "<i class='fas fa-sun'></i> Light"
    } else {
        lighter()
        dark = true
        document.getElementById("toggle-btn").innerHTML = '<i class="fas fa-moon"></i> Dark'
    }
}

function darker() {
    document.getElementById("git").style.filter = github_logo_filter;
    document.getElementById("right").style.backgroundColor = right_division_bg;
    document.getElementById("texttt").style.textShadow = Above_text_writer_text_shadow;
    document.getElementById("texttt").style.color = "white";
    document.getElementById("typed").style.color = The_typewriter_text_color;
    document.getElementById("left").style.backgroundColor = right_division_bg;
    document.querySelector("p").style.color = p_tag_color;
    document.getElementsByClassName("form")[0].style.backgroundColor = chatform_background_color;
    document.getElementsByClassName("form")[0].style.border = chatform_border;
    document.getElementsByClassName("chat_input")[0].style.backgroundColor = chat_input_box_background_color;
    document.getElementsByClassName("chat_input")[0].style.borderBottom = chat_input_borderbottom;
    document.getElementById("sendButton").style.color = send_button_font_color;
    document.getElementById("sendButton").style.backgroundColor = send_button_background_color;
    document.getElementById("form-div").style.backgroundColor = form_div_bg;
    document.getElementById("form1").style.backgroundColor = form_of_contact;
    document.getElementById("stats").src = src_of_github_readme_stats;
    document.getElementById("langs").src = src_of_github_langs;


    var tabs = document.getElementsByClassName("tablink");

    for (i = 0; i < tabs.length; i++) {
        tabs[i].style.backgroundColor = tablink$;
    };

    document.getElementById("defaultOpen").click();
}

function lighter() {
    document.getElementById("git").style.filter = "invert(0)"
    document.getElementById("right").style.backgroundColor = "#e0ece4";
    document.getElementById("texttt").style.textShadow = "2px 2px #a3d2ca";
    document.getElementById("texttt").style.color = "#5eaaa8";
    document.getElementById("typed").style.color = "#056676";
    document.getElementById("left").style.backgroundColor = "#468684";
    document.querySelector("p").style.color = "#468684";
    document.getElementsByClassName("form")[0].style.backgroundColor = "#51adcf";
    document.getElementsByClassName("form")[0].style.border = "1px solid #51adcf";
    document.getElementsByClassName("chat_input")[0].style.backgroundColor = "#73bdd9";
    document.getElementsByClassName("chat_input")[0].style.borderBottom = "2px solid #fff";
    document.getElementById("sendButton").style.color = "#000";
    document.getElementById("sendButton").style.backgroundColor = "#3191b4";
    document.getElementById("form-div").style.backgroundColor = "#e36bae";
    document.getElementById("form1").style.backgroundColor = "#f8a1d1";
    document.getElementById("stats").src = "https://github-readme-stats.vercel.app/api?username=yash-varshney-creativities&show_icons=true";
    document.getElementById("langs").src = "https://github-readme-stats.vercel.app/api/top-langs/?username=yash-varshney-creativities";

    var tabs = document.getElementsByClassName("tablink");

    for (i = 0; i < tabs.length; i++) {
        tabs[i].style.backgroundColor = "#5eaaa8"
    };


    document.getElementById("defaultOpen").click();
};