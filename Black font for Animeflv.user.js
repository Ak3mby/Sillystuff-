// ==UserScript==
// @name           Black font (Animeflv)
// @namespace      http://tampermonkey.net/
// @description    No need for userstyles, just crappy gui with plain black background
// @version        test1
// @author         Ak3mby(Akemby)
// @icon           https://media.discordapp.net/attachments/1201846119592898650/1295509104311275581/fun-lil-icon-i-made-v0-6901euj8t7ab1.png?ex=670ee85f&is=670d96df&hm=94989f9e9bc49c58062a8366aeed8f4588840b764d42990a5645f87828f704e4&=&format=webp&quality=lossless&width=428&height=428
// @match          https://www3.animeflv.net/*
// ==/UserScript==
let font = document.querySelector("head > link:nth-child(15)")
font.remove()
document.body.style.backgroundColor = "#000000";
