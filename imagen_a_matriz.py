from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Abre la imagen
imagen = Image.open('imagen.jpg')

# Convierte la imagen a escala de grises (opcional)
imgGray = imagen.convert("L")
matriz = np.asarray(imgGray)

print(matriz)
plt.imshow(imgGray, cmap="gray")
plt.show()