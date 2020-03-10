function optionchange() {
    var opt = document.querySelector("#sel_option").value;
    console.log('*** opt ',opt);

    var from = document.querySelector("#row-from");
    var to = document.querySelector("#row-to");    
    if( opt === "One" || opt === "From") {
        if( from.classList.contains('hidden')) from.classList.toggle('hidden');
        if( !to.classList.contains('hidden')) to.classList.toggle('hidden');
    } else if (opt === "To") {
        if( to.classList.contains('hidden')) to.classList.toggle('hidden');
        if( !from.classList.contains('hidden')) from.classList.toggle('hidden');
    } else if (opt === "FromTo") {
        if( from.classList.contains('hidden')) from.classList.toggle('hidden');
        if( to.classList.contains('hidden')) to.classList.toggle('hidden');
    } else {
        if( !from.classList.contains('hidden')) from.classList.toggle('hidden');
        if( !to.classList.contains('hidden')) to.classList.toggle('hidden');
    }

}
