from PIL import Image
from io import BytesIO
import os


def comprimir_imagen(ruta_origen, ruta_destino, calidad=40, max_size_kb=100):
    # Abrimos la imagen
    img = Image.open(ruta_origen)
    img = img.convert("RGB")

    # Creamos un buffer
    output = BytesIO()
    img.save(output, format="JPEG", quality=calidad, optimize=True)
    output.seek(0)

    # Verificamos el tamaño comprimido
    tamaño_comprimido = len(output.getvalue())
    print(f"Tamaño final: {tamaño_comprimido / 1024:.2f} KB")

    if tamaño_comprimido <= max_size_kb * 1024:
        with open(ruta_destino, "wb") as f:
            f.write(output.read())
        print("✅ Imagen comprimida y guardada.")
    else:
        print("⚠️ Comprimida, pero aún supera el límite deseado.")


# Reemplazá esto por la ruta de tu imagen real
comprimir_imagen("imagen_22mb.jpg", "comprimida.jpg")
