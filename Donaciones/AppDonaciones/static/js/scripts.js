function normalizeText(text) {
    return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}


function exportTableToExcel() {
  const table = document.querySelector("table");
  const rows = Array.from(table.querySelectorAll("tr"));

  const data = rows.map(row => {
      const cells = Array.from(row.querySelectorAll("td, th"));
      return cells
          .filter((cell, index) => index !== 2 && index !== cells.length - 1) // Excluye la 3ra y la última columna
          .map(cell => {
              const textarea = cell.querySelector("textarea");
              return textarea ? textarea.value : cell.textContent.trim();
          });
  });

  // Pedir al usuario un nombre para el archivo
  let fileName = prompt("Ingrese el nombre del archivo (sin extensión):", "listado-de-donaciones");
  if (!fileName) {
      alert("Exportación cancelada.");
      return;
  }

  // Asegurar la extensión .xlsx
  if (!fileName.endsWith(".xlsx")) {
      fileName += ".xlsx";
  }

  // Generar el archivo Excel con SheetJS
  const ws = XLSX.utils.aoa_to_sheet(data);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Tabla Exportada");
  XLSX.writeFile(wb, fileName);
}


function chopearPalabraFinal(texto, palabra) {
  let regex = new RegExp(palabra + "$"); // Expresión regular para buscar la palabra al final
  return texto.replace(regex, "").trim(); // Reemplaza la palabra por vacío y quita espacios extra
}

function handleWhatsAppClick(button) {
    // Encuentra la fila más cercana al botón
    const row = button.closest("tr");
    const cells = row.querySelectorAll("td");

    // Verifica si la fila tiene suficientes celdas
    if (cells.length > 1) {
        const titulo = cells[1].textContent.trim();  // Segunda celda
        const descripcion = cells[2].textContent.trim();  // Tercera celda
        const propietario = cells[cells.length - 3].textContent.trim(); // Antepenúltima celda
        var phone = cells[cells.length - 2].textContent.trim(); // Anteúltima celda
        const message = "Hola " + propietario + ", me comunico con respecto a su donación: " + titulo + ". " + descripcion + ". ";
        
        if (phone) {
            phone = chopearPalabraFinal(phone, "Contactar");
            if (phone.slice(0, 3) !== "549") {
              phone = "549" + phone;
            }
            const whatsappUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
            window.open(whatsappUrl, "_blank"); // Abre WhatsApp Web
        } else {
            alert("No se encontró un número de teléfono válido en esta fila.");
        }
    } else {
        alert("Error: No se pudo encontrar el número de teléfono.");
    }
}


function validarContrasenia(event, contraseniaCorrecta) {
  event.preventDefault(); // Previene que el formulario se envíe automáticamente

  let inputContrasenia = document.getElementById('contrasenia').value;
  let errorMsg = document.getElementById('error-msg');

  if (inputContrasenia !== contraseniaCorrecta) {
      errorMsg.style.display = 'block';
      return false;  // Detiene el envío del formulario
  }

  errorMsg.style.display = 'none';
  event.target.submit();  // Envía el formulario manualmente si la contraseña es correcta
}


function inputChange()
{
  var errorMsg = document.getElementById("error-msg");
  errorMsg.style.display = "none";
}


document.getElementById("load-more").addEventListener("click", function (event) {
  event.preventDefault(); // Evita que la página suba
});
let page = 1;
let query = "";


function buscarDonaciones() {
    query = document.getElementById("search-input").value;
    page = 1;
    document.getElementById("tableBody").innerHTML = ""; // Limpia resultados anteriores
    cargarMas();
}

function cargarMas() {
    const donacionesList = document.getElementById('tableBody');
    
    var botonCargarMas = document.getElementById('load-more');
    botonCargarMas.className = "btn btn-sm btn-primary";
    botonCargarMas.disabled = false;
    botonCargarMas.innerText = "Cargar más";
    
    // FECHAS //
    fetch(`/buscar/?q=${query}&page=${page}`, {
        headers: { "X-Requested-With": "XMLHttpRequest" } // Indica que es una petición AJAX
    })
    .then(response => response.json())
    .then(data => {
        data.donaciones.forEach(donacion => {
            const fechaISO = donacion.fecha_creacion;
            // const fechaLocal = new Date(fechaISO).toLocaleString();
            if (donacion.imagen) {
                var ruta_imagen = "/static/" + donacion.imagen;    
            }
            else {
                var ruta_imagen = "/static/assets/img/sin-imagen.jpg" + donacion.imagen;
            }
            const fecha = new Date(fechaISO);
            const formato = fecha.toLocaleString("es-AR", {
                year: "numeric",
                month: "2-digit",
                day: "2-digit",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit"
            });
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${formato}</td>
                <td>${donacion.titulo}</td>
                <td>${donacion.descripcion}</td>
                <td>${donacion.imagen}</td>
                <td><img class="img-fluid mb-3 rounded" style="width: 90%; height: auto;" src=${ruta_imagen} alt="Imagen"></td>
                <td>${donacion.propietario}</td>
                <td>${donacion.telefono}
                  <a class="anchor-whatsapp" onclick="handleWhatsAppClick(this)">Contactar</a>
                </td>
                <td class="py-4 px-6">
                  <a class="btn btn-primary btn-xs" href="http://127.0.0.1:8000/editarDonacion/${donacion.id}">Editar</a>
                  <a class="btn btn-danger btn-xs" href="http://127.0.0.1:8000/eliminarDonacion/${donacion.id}">Borrar</a>
                </td>
            `;
            donacionesList.appendChild(tr);
        });

        if (data.has_next) {
            document.getElementById("load-more").style.display = "block";
        } else {
            botonCargarMas.disabled = true;
            botonCargarMas.innerText = "No hay más elementos";
            botonCargarMas.className = "btn btn-light";            
        }

        page++;
    });
}
cargarMas();


function detectarEnter(event) {
  if (event.key === "Enter") { // Detecta si la tecla presionada es "Enter"
      buscarDonaciones(); // Llama a la función de búsqueda
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const boton = document.querySelector("#miBoton");
  if (boton) {
      boton.addEventListener("click", function() {
          console.log("Botón clickeado");
      });
  }
    const btnRecuperar = document.querySelector(".anchor-recuperar-contrasenia");
   
    if (btnRecuperar) {
          alert("HOLA");
          btnRecuperar.addEventListener("click", function () {
              document.body.style.cursor = "wait"; // Cambia el cursor a "cargando"
              
              // Opcional: Deshabilitar el botón mientras se carga
              this.style.pointerEvents = "none"; 
              this.style.opacity = "0.7"; // Darle una apariencia de "deshabilitado"
              
              // Restaurar cursor después de 3 segundos (si la nueva página tarda en cargar)
              setTimeout(() => {
                  document.body.style.cursor = "default"; 
                  this.style.pointerEvents = "auto"; 
                  this.style.opacity = "1";
              }, 3000);
          });
    } 
});

// document.addEventListener("DOMContentLoaded", function () {
//   const enlaceRecuperar = document.querySelector(".anchor-recuperar-contrasenia");

//   if (enlaceRecuperar) {
//       enlaceRecuperar.addEventListener("click", function (event) {
//           event.preventDefault(); // Evita que el enlace funcione inmediatamente
//           this.style.cursor = "wait"; // Cambia el cursor a "cargando"
//           this.style.pointerEvents = "none"; // Deshabilita el enlace
//           this.style.opacity = "0.6"; // Reduce la opacidad para indicar que está deshabilitado

//           alert("SII");

//           // Opcional: Restaurar después de 3 segundos si es necesario
//           setTimeout(() => {
//               this.style.cursor = "pointer"; // Vuelve al cursor normal
//               this.style.pointerEvents = "auto"; // Reactiva el enlace
//               this.style.opacity = "1";
//               window.location.href = this.href; // Redirige manualmente al enlace
//           }, 3000);
//       });
//   }
// });

function esperar() {
  const enlaceRecuperar = document.querySelector(".anchor-recuperar-contrasenia");
  document.body.style.cursor = "wait"; // Cambia el cursor a "cargando"
  enlaceRecuperar.style.pointerEvents = "none"; // Deshabilita el enlace
  enlaceRecuperar.style.opacity = "0.1";
}

// const maxWidthCellphone = 1368;
// if (screen.width <= maxWidthCellphone) {
//     const footer = document.getElementById('footer');
//     const footer_1 = document.getElementById('footer-1');
//     footer.style.display = 'none';
//     footer_1.style.display = 'none';
// }