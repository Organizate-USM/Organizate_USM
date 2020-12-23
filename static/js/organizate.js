          
          
          
          
    // Your web app's Firebase configuration
    var firebaseConfig = {
        apiKey: "AIzaSyD7geC0GEHTf9vREokkJGRRkad5BETp5q0",
        authDomain: "organizateusm.firebaseapp.com",
        projectId: "organizateusm",
        storageBucket: "organizateusm.appspot.com",
        messagingSenderId: "950537281109",
        appId: "1:950537281109:web:86dd2cd4dead3496053edc"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);


    //A
    var username;
    username = document.getElementById('user').value;

    function addItemsToList(text,complete){

        var ul = document.getElementById('myUL');
        var a = document.getElementById("iden"+text)
        var firstA = document.createElement('a');
        firstA.classList.add('boton-todo');
        firstA.setAttribute("onclick",`check("${text}",${complete})`);
        var spanCloseLeft = document.createElement('span');
        spanCloseLeft.innerHTML= '   ✔';


        if(complete == false){
        spanCloseLeft.classList.add('closeleft');
        var _text = document.createElement('li');
        _text.classList.add('lito');
        _text.setAttribute("id", "iden"+text);
        _text.innerHTML= text;

        firstA.appendChild(spanCloseLeft);

        _text.appendChild(firstA);

        ul.appendChild(_text);
        }
        
        else{
        spanCloseLeft.classList.add('closeleft-check');
        var _complete = document.createElement('li');
        _complete.classList.add('checked');
        _complete.setAttribute("id", "idenCheked"+text);
        _complete.innerHTML= text;

        var secondA = document.createElement('a');
        secondA.classList.add('boton-delete');
        secondA.setAttribute("onclick",`del("${text}")`)
        var spanClose = document.createElement('span');
        spanClose.classList.add('close');
        spanClose.innerHTML= 'X';

        firstA.appendChild(spanCloseLeft);
        secondA.appendChild(spanClose);
        _complete.appendChild(secondA);
        _complete.appendChild(firstA);

        ul.appendChild(_complete);

        }

    }


    function RemoveItemsToList(){
        var ul = document.getElementById('myUL');
        var list = document.getElementsByClassName('lito');
        var checked = document.getElementsByClassName('checked');

        var largoList = list.length;
        var largoChecked = checked.length;

        for(i = 0; i< largoList; i++){
            ul.removeChild(list.item(0));    
        }
        for(i = 0; i< largoChecked; i++){
            ul.removeChild(checked.item(0));    
        }

      
    }

    function FetchAllData(){
        // arrr = {{ listaEvento }}
        // console.log(arrr);
        firebase.database().ref(`user/${username}/todolist`).once('value',function(snapchot){
            snapchot.forEach(
                function(childSnapchot){
                    let texto = childSnapchot.val().Description;
                    let complete = childSnapchot.val().Checked;
                    var comprobar = document.getElementById("iden"+texto)
                    var comprobarCheck = document.getElementById("idenCheked"+texto)
                    if(comprobar == null && comprobarCheck == null){
                        addItemsToList(texto,complete);
                    }
                    
                }
            );
        });
    }
    
    function getDatos(text){
        function getDatos(text){
        var ref = firebase.database().ref("student/"+text);
        ref.once("value")
        .then(function(snapshot) {
            var checked = snapshot.child("Checked").val();
            return checked;
        });
    }
    }

    //Read
    var text,complete;
       
    function Ready(){
        text = document.getElementById('myInput').value;
    }

    //Insert

    document.getElementById('addBtn').onclick = function(){
        console.log("toiaca");
        Ready();
        firebase.database().ref(`user/${username}/todolist/${text}`).set({
            Description: text,
            Checked: false
        });

        FetchAllData();
        // RemoveItemsToList();
        // window.onload(FetchAllData());
    }
    //Check

    function check(text,complete){
        var ul = document.getElementById('myUL');
        if (complete == false) {
        var elemento = document.getElementById("iden"+text);
        ul.removeChild(elemento);

        firebase.database().ref(`user/${username}/todolist/${text}`).update({
            Checked: true
            });
            FetchAllData();
        }
        
        else{
            var elemento = document.getElementById("idenCheked"+text);
            ul.removeChild(elemento);
            firebase.database().ref(`user/${username}/todolist/${text}`).update({
            Checked: false
            });
            FetchAllData();
        }

        // reload();
        // RemoveItemsToList();
        // window.onload(FetchAllData());
    }


    //Delete 

    function del(text){
        firebase.database().ref(`user/${username}/todolist/${text}`).remove();
        var ul = document.getElementById('myUL');
        var elemento = document.getElementById("idenCheked"+text);
        ul.removeChild(elemento);
        FetchAllData();

    }
    
    function reload(){
        $(document).ready(function(){
            $("#div-myul").load("todolist")
            FetchAllData();
        });
    }