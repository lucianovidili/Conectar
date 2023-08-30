//Seteo a Jugadores, DT's y Clubes para que solo se muestren si se "hoverea" sobre dicha palabra y no el área de abajo.
let jugadoresDespList = document.getElementById('jugadoresDespList');
let dropDownListPilares = document.getElementById('dropJugadores');
jugadoresDespList.addEventListener('mouseover', function() {dropDownListPilares.style.visibility = 'visible';});
jugadoresDespList.addEventListener('mouseleave', function() {dropDownListPilares.style.visibility = 'hidden';});

let dtsDespList = document.getElementById('dtsDespList');
let dropDownListDts = document.getElementById('dropDts');
dtsDespList.addEventListener('mouseover', function() {dropDownListDts.style.visibility = 'visible';});
dtsDespList.addEventListener('mouseleave', function() {dropDownListDts.style.visibility = 'hidden';});

let clubesDespList = document.getElementById('clubesDespList');
let dropDownListClubes = document.getElementById('dropClubes');
clubesDespList.addEventListener('mouseover', function() {dropDownListClubes.style.visibility = 'visible';});
clubesDespList.addEventListener('mouseleave', function() {dropDownListClubes.style.visibility = 'hidden';});