
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

    function addItemsToList(text,complete){

        var ul = document.getElementById('myUL');

        var firstA = document.createElement('a');
        firstA.classList.add('boton-todo');
        firstA.setAttribute("onclick",`check("${text}",${complete})`);
        var spanCloseLeft = document.createElement('span');
        spanCloseLeft.innerHTML= '   ✔';


        if(complete == false){
        spanCloseLeft.classList.add('closeleft');
        var _text = document.createElement('li');
        _text.classList.add('lito');
        _text.innerHTML= text;

        firstA.appendChild(spanCloseLeft);

        _text.appendChild(firstA);

        ul.appendChild(_text);
        }
        
        else{
        spanCloseLeft.classList.add('closeleft-check');
        var _complete = document.createElement('li');
        _complete.classList.add('checked');
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

    function olal(){
        console.log("S")
    }

    function RemoveItemsToList(){
        var ul = document.getElementById('myUL');
        var list = document.getElementsByClassName('lito');
        var checked = document.getElementsByClassName('checked');
        console.log(list);
        console.log(checked);

        var largoList = list.length;
        var largoChecked = checked.length;

        for(i = 0; i< largoList; i++){
            ul.removeChild(list.item(0));    
            console.log(i) 
        }
        for(i = 0; i< largoChecked; i++){
            ul.removeChild(checked.item(0));    
            console.log(i) 
        }

      
    }

    function FetchAllData(){
        firebase.database().ref(`user/${username}/todolist`).once('value',function(snapchot){
            snapchot.forEach(
                function(childSnapchot){
                    let texto = childSnapchot.val().Description;
                    let complete = childSnapchot.val().Checked;
                    addItemsToList(texto,complete);
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
    
    function initial(){
        console.log(username);
    }
        
    function Ready(){
        text = document.getElementById('myInput').value;
    }

    //Insert

    document.getElementById('addBtn').onclick = function(){
        Ready();
        firebase.database().ref(`user/${username}/todolist/${text}`).set({
            Description: text,
            Checked: false
        });
        RemoveItemsToList();
        window.onload(FetchAllData());
    }

    //Check

    function check(text,complete){
        console.log(complete);
        if (complete == false) {
        firebase.database().ref(`user/${username}/todolist/${text}`).update({
            Checked: true
        });
        }
        
        else{
            firebase.database().ref(`user/${username}/todolist/${text}`).update({
            Checked: false
        }); 
        }

        RemoveItemsToList();
        window.onload(FetchAllData());
    }


    //Delete 

    function del(text){
        firebase.database().ref(`user/${username}/todolist/${text}`).remove();
        RemoveItemsToList();
        window.onload(FetchAllData());
    }
    initial();
    window.onload(FetchAllData());