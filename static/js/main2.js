// Variables requeridas
var session_seconds = "00";
var session_minutes = 5;

// Audios
var click_sound = new Audio("static/audio/click.mp3");
var bell = new Audio("static/audio/bell.mp3");


function template() {
    document.getElementById("minutes").innerHTML = session_minutes;
    document.getElementById("seconds").innerHTML = session_seconds;
}

function start_timer() {
    click_sound.play();

    // Cambio de los mintuos y segundos del incio
    session_minutes = 00;
    session_seconds = 05;

    // Agrega los segundos y minutos a la pagina 
    document.getElementById("minutes").innerHTML = session_minutes;
    document.getElementById("seconds").innerHTML = session_seconds;

    // Inicia el conteo
    var minutes_interval = setInterval(minutesTimer, 60000);
    var seconds_interval = setInterval(secondsTimer, 1000);

    //Función para los minutos
    function minutesTimer() {
        session_minutes = session_minutes - 1;
        document.getElementById("minutes").innerHTML = session_minutes;
    }

    //Función para los segundos
    function secondsTimer() {
        session_seconds = session_seconds - 1;
        document.getElementById("seconds").innerHTML = session_seconds;

        // Revisa si los minutos y segundos llegan a 0
        // Si llega a 0:
        if (session_seconds <= 0) {
            if (session_minutes <= 0) {
                // Para el contador y terminan los intervalos
                clearInterval(minutes_interval); 
                clearInterval(seconds_interval);

                // Agrega el mensaje al html
                document.getElementById("done").innerHTML =
                "¡Descanso finalizado!, vuelve al trabajo/estudio";
                document.getElementById("trabajo").innerHTML =
                "Dirígete al timer de trabajo aquí";
                

                // Hace el mensaje visible
                document.getElementById("done").classList.add("show_message");
                document.getElementById("trabajo").classList.add("show_message");
                

                // Suena la campana
                bell.play();
        }

        // Resetea los segundos a 60
            session_seconds = 60;
        }
    }
}
