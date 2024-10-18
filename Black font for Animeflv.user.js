// ==UserScript==
// @name           Black font (Animeflv)
// @namespace      http://tampermonkey.net/
// @description    No need for userstyles, just crappy gui with plain black background
// @version        test1
// @author         Ak3mby(Akemby)
// @icon           https://cdn.discordapp.com/icons/1296915461954470058/bf720ede6b8c239672ce5d2e4873ae14.webp?size=100&quo
// @match          https://www3.animeflv.net/*
// ==/UserScript==
let font = document.querySelector("head > link:nth-child(15)")
font.remove()
document.body.style.backgroundColor = "#000000";
