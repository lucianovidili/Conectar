function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const tableBody = document.getElementById("tableBody");
    const rows = tableBody.getElementsByTagName("tr");
    let hasVisibleRows = false;
  
    // Función para verificar coincidencias al inicio de palabras
    function matchesStartOfWords(text, filter) {
      const words = text.split(/\s+/); // Divide el texto en palabras por espacios
      return words.some(word => word.startsWith(filter)); // Verifica si alguna palabra comienza con el filtro
    }
  
    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("td");
      let rowMatches = false;
  
      if (cells.length > 0) { // Ignorar el mensaje "sin resultados"
        for (let j = 0; j < cells.length; j++) {
          const cellText = cells[j].innerText.toLowerCase();
          const textarea = cells[j].querySelector("textarea");
          const textareaContent = textarea ? textarea.value.toLowerCase() : "";
  
          // Verificar coincidencias al inicio de palabras en el texto de la celda o el contenido del textarea
          if (matchesStartOfWords(cellText, filter) || matchesStartOfWords(textareaContent, filter)) {
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


function exportTableToExcel() {
    const table = document.querySelector("table");
    const rows = Array.from(table.querySelectorAll("tr"));

    const data = rows.map(row => {
        const cells = Array.from(row.querySelectorAll("td, th"));
        return cells.slice(0, -2).map(cell => { // Excluye las últimas dos columnas con slice
            const textarea = cell.querySelector("textarea");
            // Si hay un <textarea>, toma su valor; de lo contrario, usa el texto del <td>
            return textarea ? textarea.value : cell.textContent.trim();
        });
    });

    // Pedir al usuario un nombre para el archivo
    let fileName = prompt("Ingrese el nombre del archivo (sin extensión):", "listado-de-donaciones");
    if (!fileName) {
        alert("Exportación cancelada.");
        return;
    }

    // Asegurarse de que el archivo tenga la extensión .xlsx
    if (!fileName.endsWith(".xlsx")) {
        fileName += ".xlsx";
    }

    // Usa SheetJS para generar el archivo Excel
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
        const phone = cells[cells.length - 2].textContent.trim(); // Anteúltima celda
        const message = "Hola, me comunico con respecto a su donación: " + titulo + ". ";

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