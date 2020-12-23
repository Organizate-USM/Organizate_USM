

// document.getElementById('addBtn-modal').onclick = function(){
//     option(0);
//     // var colorbtn = document.getElementById('color').value;
//     // var fecha = document.getElementById('cal-date').value;
//     // var nombre = document.getElementById('cal-text').value;
//     // var descripcion = document.getElementById('cal-desc').value;
//     // console.log(colorbtn)
//     // firebase.database().ref(`user/${username}/calendary/${fecha}`).set({
//     //     NombreEvento: nombre,
//     //     Descripcion: descripcion,
//     //     FechaEvento: fecha,
//     //     Color: colorbtn,
//     //     });
//     // reloadCalendary()
//     // printEvent()
// }

function option(cont){
    console.log("a");
    fecha = document.getElementById('cal-date').value;
    var ref = firebase.database().ref(`user/${username}/calendary/${fecha}-${cont}`);
    ref.once("value")
        .then(function(snapshot) {
        var existe = snapshot.exists();
        insertar(existe,fecha,cont);
        
  });
}

function insertar(existe,fecha,cont){
    if(existe == false){
        var nombre = document.getElementById('cal-text').value;
        var descripcion = document.getElementById('cal-desc').value;
        var colorbtn = document.getElementById('color').value;
        var version = cont;
        firebase.database().ref(`user/${username}/calendary/${fecha}-${cont}`).set({
            NombreEvento: nombre,
            Descripcion: descripcion,
            FechaEvento: fecha,
            Color: colorbtn,
            Version: version
            });
        reloadCalendary()
        printEvent()
    }
    else{
        cont++;
        option(cont)
    }
}

function delEvent(fecha,version){
    firebase.database().ref(`user/${username}/calendary/${fecha}-${version}`).remove();
    var ul = document.getElementById('ul-model');
    var elemento = document.getElementById(`calen${fecha}-${version}`);
    ul.removeChild(elemento);
    reloadCalendary()
    printEvent()
    

}


function addLiCalendar(fecha, nombre, version){

    var ul = document.getElementById('ul-model');
    var firstA = document.createElement('a');
    firstA.setAttribute("onclick",`delEvent("${fecha}",${version})`);
    var span = document.createElement('span');
    span.classList.add("close-del")
    span.innerHTML= 'X';

    var listad = fecha.split("-");
    var mesesSpanish = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    var mesSpanish = mesesSpanish[parseInt(listad[1])-1]
    var fechaleer = `${nombre}, Fecha: ${listad[2]} de ${mesSpanish} del ${listad[0]}`

    var evento = document.createElement('li');
    evento.classList.add('lito-modal');
    evento.setAttribute("id", `calen${fecha}-${version}`);
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
                let version = childSnapchot.val().Version;
                var comprobar = document.getElementById(`calen${fecha}-${version}`)
                if(comprobar == null){
                    addLiCalendar(fecha,nombre,version);
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

