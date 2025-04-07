from PIL import Image
import numpy as np

# Reducimos un poco el tamaño
width, height = 6000, 6000

# Generamos una imagen aleatoria
array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(array)

# Guardamos con calidad 90 (buena, pero más comprimida)
image.save("imagen_22mb.jpg", "JPEG", quality=30)
