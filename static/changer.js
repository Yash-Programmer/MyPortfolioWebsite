document.getElementById("texttt").style.color = "white";
var right_division_bg = document.getElementById("right").style.backgroundColor,
    left_division_bg = document.getElementById("left").style.backgroundColor,
    Above_text_writer_text_shadow = document.getElementById("texttt").style.textShadow,
    Above_text_writer_text_color = document.getElementById("texttt").style.color,
    The_typewriter_text_color = document.getElementById("typed").style.color,
    tablink$ = document.getElementsByClassName("tablink"),
    p_tag_color = document.querySelector("p").style.color,
    form_div_bg = document.getElementById("form-div").style.backgroundColor,
    form_of_contact = document.getElementById("form1").style.backgroundColor,
    chatform_background_color = document.getElementsByClassName("form")[0].style.backgroundColor,
    chatform_border = document.getElementsByClassName("form")[0].style.border,
    chat_input_box_background_color = document.getElementsByClassName("chat_input")[0].style.backgroundColor,
    chat_input_borderbottom = document.getElementsByClassName("chat_input")[0].style.borderBottom,
    send_button_font_color = document.getElementById("sendButton").style.color,
    send_button_background_color = document.getElementById("sendButton").style.backgroundColor,
    src_of_github_readme_stats = document.getElementById("stats").src,
    src_of_github_langs = document.getElementById("langs").src,
    dark = false

function changer() {
    if (dark === true) {
        dark = false
        darker()
    } else {
        dark = true
        lighter()
    }

}

function darker() {
    document.getElementById("right").style.backgroundColor = right_division_bg
    document.getElementById("texttt").style.textShadow = Above_text_writer_text_shadow
    document.getElementById("texttt").style.color = "white"
    document.getElementById("typed").style.color = The_typewriter_text_color
    document.getElementById("left").style.backgroundColor = right_division_bg
    document.querySelector("p").style.color = p_tag_color
    document.getElementsByClassName("form")[0].style.backgroundColor = chatform_background_color
    document.getElementsByClassName("form")[0].style.border = chatform_border
    document.getElementsByClassName("chat_input")[0].style.backgroundColor = chat_input_box_background_color
    document.getElementsByClassName("chat_input")[0].style.borderBottom = chat_input_borderbottom
    document.getElementById("sendButton").style.color = send_button_font_color
    document.getElementById("sendButton").style.backgroundColor = send_button_background_color
    document.getElementById("form-div").style.backgroundColor = form_div_bg
    document.getElementById("form1").style.backgroundColor = form_of_contact
    document.getElementById("stats").src = src_of_github_readme_stats
    document.getElementById("langs").src = src_of_github_langs;
    var t = document.getElementsByClassName("tablink");
    for (i = 0; i < t.length; i++) t[i].style.backgroundColor = tablink$;
    document.getElementById("defaultOpen").click()
    dark = false
}

function lighter() {
    document.getElementById("right").style.backgroundColor = "#e0ece4", document.getElementById("texttt").style.textShadow = "2px 2px #a3d2ca", document.getElementById("texttt").style.color = "#5eaaa8", document.getElementById("typed").style.color = "#056676", document.getElementById("left").style.backgroundColor = "#468684", document.querySelector("p").style.color = "#468684", document.getElementsByClassName("form")[0].style.backgroundColor = "#51adcf", document.getElementsByClassName("form")[0].style.border = "1px solid #51adcf", document.getElementsByClassName("chat_input")[0].style.backgroundColor = "#73bdd9", document.getElementsByClassName("chat_input")[0].style.borderBottom = "2px solid #fff", document.getElementById("sendButton").style.color = "#000", document.getElementById("sendButton").style.backgroundColor = "#3191b4", document.getElementById("form-div").style.backgroundColor = "#e36bae", document.getElementById("form1").style.backgroundColor = "#f8a1d1", document.getElementById("stats").src = "https://github-readme-stats.vercel.app/api?username=yash-programmer&show_icons=true", document.getElementById("langs").src = "https://github-readme-stats.vercel.app/api/top-langs/?username=yash-programmer";
    var t = document.getElementsByClassName("tablink");
    for (i = 0; i < t.length; i++) t[i].style.backgroundColor = "#5eaaa8";
    document.getElementById("defaultOpen").click()
    dark = true
}