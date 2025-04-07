from django.db import models
from django.utils.timezone import now
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from django.core.files.base import ContentFile
import os
import pillow_heif

# Para soporte HEIC → JPG
try:
    import pillow_heif

    pillow_heif.register_heif_opener()
except ImportError:
    print("⚠️ pillow_heif no está instalado. No se podrá convertir HEIC.")


RAW_EXTENSIONS = [".cr2", ".nef", ".arw", ".rw2", ".dng", ".orf", ".sr2"]


class Donacion(models.Model):
    fecha_creacion = models.DateTimeField(default=now, blank=True, null=True)
    titulo = models.CharField(max_length=90, null=False, blank=False)
    # transferible = models.CharField(max_length=10, choices=transferible_opciones, default='no', verbose_name='Transferible')
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(
        upload_to="assets/img/donaciones",
        null=True,
        blank=True,
    )
    propietario = models.CharField(max_length=90, null=False, blank=False)
    telefono = models.IntegerField(blank=False, null=False)
    contrasenia = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Contraseña"
    )
    email = models.EmailField(max_length=254, verbose_name="E-mail", unique=False)

    def save(self, *args, **kwargs):
        if self.imagen:
            try:
                extension = os.path.splitext(self.imagen.name)[1].lower()

                # RAW: Rechaza .cr2, .nef, etc.
                raw_extensiones = [".cr2", ".nef", ".raw", ".arw", ".dng"]
                if extension in raw_extensiones:
                    raise ValueError("El formato RAW no está permitido.")

                # HEIC → convertir a JPG
                if extension == ".heic":
                    heif_file = pillow_heif.read_heif(self.imagen)
                    img = Image.frombytes(
                        heif_file.mode, heif_file.size, heif_file.data, "raw"
                    )
                    img = img.convert("RGB")
                    output = BytesIO()
                    img.save(output, format="JPEG", quality=40, optimize=True)
                    output.seek(0)
                    self.imagen = ContentFile(output.read(), name="convertida.jpg")

                # Comprimir si pesa más de 100 KB
                elif self.imagen.size > 100 * 1024:
                    self.imagen.seek(0)
                    img = Image.open(self.imagen)
                    img = img.convert("RGB")
                    output = BytesIO()
                    img.save(output, format="JPEG", quality=40, optimize=True)
                    output.seek(0)
                    filename = os.path.splitext(self.imagen.name)[0] + ".jpg"
                    self.imagen = ContentFile(output.read(), name=filename)

            except UnidentifiedImageError:
                raise ValueError("Formato de imagen no soportado.")
            except Exception as e:
                raise ValueError(f"Error al procesar la imagen: {e}")

        super().save(*args, **kwargs)
