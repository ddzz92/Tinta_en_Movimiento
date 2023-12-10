// Formulario de consulta

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
  
    form.addEventListener("submit", function(event) {
      let nombreInput = form.querySelector('input[name="nombre"]');
      let emailInput = form.querySelector('input[name="email"]');
      let consultaTextarea = form.querySelector('textarea[name="consulta"]');
      
      const nombreApellido = nombreInput.value.trim();
      const email = emailInput.value.trim();
      const consulta = consultaTextarea.value.trim();
      
      if (!/^[A-ZÁÉÍÓÚÜÑa-záéíóúüñ\s]+$/.test(nombreApellido)) {
        alert("El formato para Nombre y apellido ingresado es incorrecto, por favor, coloca tu nombre y apellido iniciando con mayúscula y con espacios.");
        event.preventDefault();
        return;
      }
      
      if (!/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/.test(email)) {
        alert("El formato para Dirección de correo ingresado es incorrecto, por favor, coloca tu dirección de correo con el siguiente formato 'correoejemplo@servicio.com'.");
        event.preventDefault();
        return;
      }
      
      if (consulta === "" || consulta.length < 50 || /[\W\d_]+/.test(consulta)) {
        alert("Por favor, realiza tu consulta con al menos 50 caracteres.");
        event.preventDefault();
        return;
      }
    });
  });

// Función de la sección Cotizador

function cotizador(tamañoLargo, tamañoAncho, colores, tinta, detalle) {
    let valor = 0;

    const largo = () => tamañoLargo * 8000;
    const ancho = () => tamañoAncho * 8000;
    const color = () => colores * 10000;
    const tintas = () => tinta * 10000;
    const detalles = () => detalle * 12000;

    valor = largo() + ancho() + color() + tintas() + detalles();
    return valor;
}

const formulario = document.getElementById("formularioCotizador");

formulario.addEventListener("submit", function (event) {
    event.preventDefault();

    const tamañoLargo = parseFloat(document.querySelector('select[name="tamaño-largo"]').value);
    const tamañoAncho = parseFloat(document.querySelector('select[name="tamaño-ancho"]').value);
    const colores = parseFloat(document.querySelector('select[name="colores"]').value);
    const tinta = parseFloat(document.querySelector('select[name="tinta"]').value);
    const detalle = parseFloat(document.querySelector('select[name="detalle"]').value);

    if (isNaN(tamañoLargo) || isNaN(tamañoAncho) || isNaN(colores) || isNaN(tinta) || isNaN(detalle)) {
        const resultadoElement = document.getElementById("resultado");
        resultadoElement.textContent = "Selecciona una opción para cada campo por favor.";
    } else {
        const valorTotal = cotizador(tamañoLargo, tamañoAncho, colores, tinta, detalle);

        const resultadoElement = document.getElementById("resultado");
        resultadoElement.textContent = `El valor total es: $${valorTotal}`;
    }
});

// Función para el botón de la barra de Menú
document.getElementById("icon-menu").addEventListener("click", mostrar_menu);

function mostrar_menu(){
    document.getElementById("move-content").classList.toggle('move-container-all');
    document.getElementById("show-menu").classList.toggle('show-lateral');
}  