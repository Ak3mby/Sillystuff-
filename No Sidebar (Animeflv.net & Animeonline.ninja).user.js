// ==UserScript==
// @name           No Sidebar (Animeflv)
// @namespace      http://tampermonkey.net/
// @description    Avoid Getting Horny by the hotties on the sidebar
// @version        test1
// @author         Ak3mby(Akemby)
// @icon           https://avatars.githubusercontent.com/u/184992787?s=400&u=34653b2f6403ab34df5491ee2ab52fe7ab34d3dc&v=4
// @match          https://www3.animeflv.net/ver/*
// @match          https://ww3.animeonline.ninja/*
// ==/UserScript==
document.querySelectorAll(".CpCnC").forEach(element => element.remove());

if (window.location.href.startsWith('https://ww3.animeonline.ninja/')) {
}
(() => {
    document.querySelector("#single > div.sidebar.right.scrolling")?.remove();
})();
