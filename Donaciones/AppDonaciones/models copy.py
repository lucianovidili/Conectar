from django.db import models
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os


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
                self.imagen.seek(0)  # Reinicia el stream
                img = Image.open(self.imagen)

                # Convertimos solo si no es JPG o pesa más de 100KB
                if self.imagen.size > 100 * 1024 or self.imagen.name.lower().endswith(
                    ".heic"
                ):
                    if img.mode != "RGB":
                        img = img.convert("RGB")

                    output = BytesIO()
                    img.save(output, format="JPEG", quality=40, optimize=True)
                    output.seek(0)

                    # Renombramos extensión a .jpg
                    filename = os.path.splitext(self.imagen.name)[0] + ".jpg"
                    self.imagen = ContentFile(output.read(), name=filename)

                    print("✔ Imagen HEIC convertida y comprimida")

            except Exception as e:
                print(f"❌ Error al procesar la imagen: {e}")

        super().save(*args, **kwargs)
