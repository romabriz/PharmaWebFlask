var formulario = document.getElementsByName('formulario')[0],
elementos = formulario.elements,
boton = document.getElementById('btn');

var validarNombre = function(e){
if (formulario.nombre.value == 0){
    alert("Complete el nombre");
    e.preventDefault();
    }
};

var validarApellido = function(e){
if (formulario.apellido.value == 0){
    alert("Complete el apellido");
    e.preventDefault();
}
};

var validarProvincia = function(e){
    if(formulario.provincia.value == "Vacio"){
        alert("Seleccione una Provincia");
        e.preventDefault();
    }
};

var validarEmail = function(e) {
    var emailInput = formulario.email.value;
    var emailRegex = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/;

    if (emailInput.trim() === "") {
        alert("Completa el campo de correo electrónico");
        e.preventDefault();
    } else if (!emailRegex.test(emailInput)) {
        alert("El formato del correo electrónico no es válido");
        e.preventDefault();
    }
};

var validarMensaje = function(e){
    if (formulario.mensaje.value == 0){
        alert("Complete el campo mensaje");
        e.preventDefault();
    }
};
                       
var validarRadio = function(e){
if (formulario.conoce[0].checked == true || formulario.conoce[1].checked == true){
} else{
    alert("Complete cómo nos conoció");
    e.preventDefault();
    }
};

var validar = function(e){
validarNombre(e);
validarApellido(e);
validarProvincia(e);
validarEmail(e);
validarMensaje(e);
validarRadio(e);

};
formulario.addEventListener("submit", validar);