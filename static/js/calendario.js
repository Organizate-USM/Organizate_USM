

    document.getElementById('addBtn-modal').onclick = function(){
        fecha = document.getElementById('cal-date').value;
        nombre = document.getElementById('cal-text').value;
        descripcion = document.getElementById('cal-desc').value;
        firebase.database().ref(`user/${username}/calendary/${fecha}`).set({
            NombreEvento: nombre,
            Descripcion: descripcion,
            FechaEvento: fecha
            });
        reloadCalendary()
        printEvent()
    }

// function option(){
//     fecha = document.getElementById('cal-date').value;
//     var ref = firebase.database().ref(`user/${username}/calendary/${fecha}-${cont}`);
//     ref.once("value")
//         .then(function(snapshot) {
//         var existe = snapshot.exists();
//         insertar(existe,fecha,cont);
        
//   });
// }

// function insertar(existe,fecha,cont){
//     if(existe == false){
//         nombre = document.getElementById('cal-text').value;
//         descripcion = document.getElementById('cal-desc').value;
//         firebase.database().ref(`user/${username}/calendary/${fecha}-${cont}`).set({
//             NombreEvento: nombre,
//             Descripcion: descripcion,
//             FechaEvento: fecha
//             });
//         reloadCalendary()
//         printEvent()
//     }
//     else{
//         cont++;
//         option(cont)
//     }
// }

function delEvent(fecha){
    firebase.database().ref(`user/${username}/calendary/${fecha}`).remove();
    var ul = document.getElementById('ul-model');
    var elemento = document.getElementById("calen"+fecha);
    ul.removeChild(elemento);
    reloadCalendary()
    printEvent()
    

}


function addLiCalendar(fecha, nombre){

    var ul = document.getElementById('ul-model');
    var firstA = document.createElement('a');
    firstA.setAttribute("onclick",`delEvent("${fecha}")`);
    var span = document.createElement('span');
    span.classList.add("close-del")
    span.innerHTML= 'X';

    listad = fecha.split("-");
    mesesSpanish = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mesSpanish = mesesSpanish[parseInt(listad[1])-1]
    fechaleer = `${nombre}, Fecha: ${listad[2]} de ${mesSpanish} del ${listad[0]}`

    var evento = document.createElement('li');
    evento.classList.add('lito-modal');
    evento.setAttribute("id", "calen"+fecha);
    evento.innerHTML= fechaleer;

    firstA.appendChild(span);

    evento.appendChild(firstA);

    ul.appendChild(evento);
    }


function printEvent(){
    firebase.database().ref(`user/${username}/calendary`).once('value',function(snapchot){
        snapchot.forEach(
            function(childSnapchot){
                let nombre = childSnapchot.val().NombreEvento;
                let fecha = childSnapchot.val().FechaEvento;
                var comprobar = document.getElementById("calen"+fecha)
                if(comprobar == null){
                    addLiCalendar(fecha,nombre);
                }
                
            }
        );
    });
}

function reloadCalendary(){
    $(document).ready(function(){
        $("#hero").load("calendary")
    });
}


window.onload(printEvent())
