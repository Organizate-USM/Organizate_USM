

function ShowEvents(){
    eventosName = [];
    eventosDate = [];
    eventosDescription = [];
    firebase.database().ref(`user/${username}/calendary`).once('value',function(snapchot){
        snapchot.forEach(
            function(childSnapchot){
                let nameEvent = childSnapchot.val().Nombre;
                let date = childSnapchot.val().Fecha;
                let description = childSnapchot.val().Descripcion;
                eventos.push(nameEvent);
                eventosDate.push(date);
                eventosDescription.push(description);
            });
    });
}
                $(document).ready(function() {
                    $('#calendar').evoCalendar({
                        calendarEvents: [{
                            id: 'event1', // Event's ID (required)
                            name: "Año nuevo", // Event name (required)
                            date: "January/1/2020", // Event date (required)
                            description: "aaaaaaaaaaaaaa",
                            type: "holiday", // Event type (required)
                            everyYear: true // Same event every year (optional)
                        },
                        {
                            name: "Vacaciones",
                            badge: "02/13 - 02/15", // Event badge (optional)
                            date: ["February/13/2020", "February/15/2020"], // Date range
                            description: "Vacaciones.", // Event description (optional)
                            type: "event",
                            color: "#63d867" // Event custom color (optional)
        
                        },
                        
                        {% for evento in event %}
                        {
                            date: `${name}`,
                            name: `${name}`,
                            description: `${description}`,
                            type: "event",
                            color: "#63d867"
                        },
                        {% endfor %}
        
                    ]
                    });
                });


                
                var comprobar = document.getElementById("iden"+texto)
                var comprobarCheck = document.getElementById("idenCheked"+texto)
                if(comprobar == null && comprobarCheck == null){
                    addItemsToList(texto,complete);
                }
                
            }
        );
    });
}