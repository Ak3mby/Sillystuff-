// Credits to Ciantic(183544) from Stack Overflow
// It works just fine with 2 as the input
(function() { if (window["_gainNode"]) { window["_gainNode"].gain.value = parseFloat(prompt('Set the playback rate')); return; } var v = document.querySelector('video'); var audioCtx = new AudioContext(); var source = audioCtx.createMediaElementSource(v); var gainNode = audioCtx.createGain(); gainNode.gain.value = parseFloat(prompt('Set the audio gain')); source.connect(gainNode); gainNode.connect(audioCtx.destination); window["_gainNode"] = gainNode; } )();
