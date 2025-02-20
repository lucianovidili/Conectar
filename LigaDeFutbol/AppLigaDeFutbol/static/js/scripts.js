function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = normalizeText(input.value.toLowerCase().trim()); // Convertir a minúsculas, eliminar espacios y normalizar
    const tableBody = document.getElementById("tableBody");
    const rows = tableBody.getElementsByTagName("tr");
    let hasVisibleRows = false;
  
    // Crear una expresión regular para buscar solo al inicio de palabras
    const regex = new RegExp(`\\b${filter}`, "i");
  
    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("td");
      let rowMatches = false;
  
      if (cells.length > 0) { // Ignorar el mensaje "sin resultados"
        for (let j = 0; j < cells.length; j++) {
          const cellText = normalizeText(cells[j].innerText.toLowerCase().trim());
          const textarea = cells[j].querySelector("textarea");
          const textareaContent = textarea
            ? normalizeText(textarea.value.toLowerCase().trim())
            : "";
  
          // Verificar si el filtro coincide solo con el inicio de palabras
          if (regex.test(cellText) || regex.test(textareaContent)) {
            rowMatches = true;
            break;
          }
        }
        rows[i].style.display = rowMatches ? "" : "none";
        if (rowMatches) hasVisibleRows = true;
      }
    }
  
    // Mostrar u ocultar el mensaje de "sin resultados"
    const noResultsMessage = document.getElementById("noResultsMessage");
    if (noResultsMessage) {
      noResultsMessage.style.display = hasVisibleRows ? "none" : "";
    }
}  
  // Función para normalizar texto y eliminar acentos
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


function handleWhatsAppClick(button) {
    // Encuentra la fila más cercana al botón
    const row = button.closest("tr");
    const cells = row.querySelectorAll("td");

    // Verifica si la fila tiene suficientes celdas
    if (cells.length > 1) {
        const titulo = cells[0].textContent.trim();  // Primera celda
        const propietario = cells[cells.length - 3].textContent.trim(); // Antepenúltima celda
        const phone = cells[cells.length - 2].textContent.trim(); // Anteúltima celda
        const message = "Hola " + propietario + ", me comunico con respecto a su donación: " + titulo + ". ";

        if (phone) {
            const whatsappUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
            window.open(whatsappUrl, "_blank"); // Abre WhatsApp Web
        } else {
            alert("No se encontró un número de teléfono válido en esta fila.");
        }
    } else {
        alert("Error: No se pudo encontrar el número de teléfono.");
    }
}


function sortTable(columnIndex) {
  let table = document.querySelector("#donations-table tbody");
  let rows = Array.from(table.querySelectorAll("tr"));

  // Obtener el estado de orden actual
  let isAscending = table.getAttribute("data-sort") !== "asc";

  rows.sort((rowA, rowB) => {
      let cellA = rowA.cells[columnIndex]?.textContent.trim() || "";
      let cellB = rowB.cells[columnIndex]?.textContent.trim() || "";

      // Evitar celdas vacías o no definidas
      if (!cellA && !cellB) return 0;
      if (!cellA) return isAscending ? 1 : -1;
      if (!cellB) return isAscending ? -1 : 1;

      // Intentar convertir a número antes de comparar
      let numA = parseFloat(cellA.replace(/,/g, "")); // Manejo de números con comas
      let numB = parseFloat(cellB.replace(/,/g, ""));

      if (!isNaN(numA) && !isNaN(numB)) {
          return isAscending ? numA - numB : numB - numA;
      } else {
          return isAscending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
      }
  });

  // Actualizar estado de orden
  table.setAttribute("data-sort", isAscending ? "asc" : "desc");

  // Reemplazar filas en la tabla
  table.innerHTML = "";
  rows.forEach(row => table.appendChild(row));
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