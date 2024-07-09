function mostrar_ocultar(id) {
  const elemento = document.getElementById(id);
  if(elemento.style.display === 'none'){
    elemento.style.display = 'block';
  }else{
    elemento.style.display = 'none'
  }
}

const logo = document.getElementById('logo');
const links = document.querySelectorAll('.navegador a:not(:first-child)');

logo.addEventListener('click', function() {
  links.forEach(link => link.classList.toggle('hidden'));
});


const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('Estas seguro de Eliminar ?')){
                e.preventDefault();
            }
        });
    });
}

function validarCampos(event) {
  event.preventDefault();
  var userValue = document.getElementById("user").value;
  var passwordValue = document.getElementById("password").value;

  if (userValue === "admin" && passwordValue === "12345") {
      window.location.assign("/CRUD");
  } else {
      alert("Usuario o contraseña incorrectos. Por favor, inténtalo nuevamente.");
      document.getElementById("user").value = "";
      passwordValue = document.getElementById("password").value = "";
  }
}
