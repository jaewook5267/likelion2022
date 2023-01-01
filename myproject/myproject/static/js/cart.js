function select_all(){
    var checkboxes = document.getElementsByName("chk");
    for(var i=0; i<checkboxes.length; i++){
        checkboxes[i].checked = true;
    }
}

function select_delete(){
    var checkboxes = document.getElementsByName("chk");
    for(var i=0; i<checkboxes.length; i++){
        checkboxes[i].checked = false;
    }
}