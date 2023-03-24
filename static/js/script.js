
// Mostrar los campos de alpha y confidence level solo si el usuario no quiere usar los valores recomendados
let respuestaInput = document.getElementById("respuesta");
let opcionDiv = document.getElementById("opcion");
respuestaInput.addEventListener("input", function() {
  if (respuestaInput.value.toLowerCase() == "n") {
    opcionDiv.style.display = "block";
  } else {
    opcionDiv.style.display = "none";
  }
});

function mostrarMensaje() {
  var mensaje = document.querySelector(".mensaje");
  mensaje.classList.add("mostrar");
  setTimeout(function() {
      mensaje.classList.remove("mostrar");
  }, 5000);
}