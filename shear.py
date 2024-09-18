import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


imagen = Image.open('imagen.jpg')
imagen_array = np.array(imagen)


sh_x = 0.5  
sh_y = 0.3  

# Matrices de cizallado
matriz_cizallado_x = np.array([
    [1, sh_x, 0],
    [0, 1, 0]
], dtype=np.float32)

matriz_cizallado_y = np.array([
    [1, 0, 0],
    [sh_y, 1, 0]
], dtype=np.float32)

# Obtener las dimensiones de la imagen
alto, ancho = imagen_array.shape[:2]

# Aplicar cizallado usando OpenCV
def aplicar_cizallado(imagen_array, matriz_cizallado):
    imagen_transformada = cv2.warpAffine(imagen_array, matriz_cizallado, (ancho, alto), flags=cv2.INTER_NEAREST)
    return imagen_transformada

# Aplicar cizallado en x
imagen_cizallada_x = aplicar_cizallado(imagen_array, matriz_cizallado_x)

# Aplicar cizallado en y
imagen_cizallada_y = aplicar_cizallado(imagen_array, matriz_cizallado_y)

# Convertir las imágenes cizalladas a PIL Image para visualizar
imagen_cizallada_x_pil = Image.fromarray(imagen_cizallada_x)
imagen_cizallada_y_pil = Image.fromarray(imagen_cizallada_y)

# Graficar la imagen original y las cizalladas
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Mostrar la imagen original
ax[0].imshow(imagen)
ax[0].set_title('Imagen Original')
ax[0].axis('off')

# Mostrar la imagen cizallada en x
ax[1].imshow(imagen_cizallada_x_pil)
ax[1].set_title('Cizallado en X')
ax[1].axis('off')

# Mostrar la imagen cizallada en y
ax[2].imshow(imagen_cizallada_y_pil)
ax[2].set_title('Cizallado en Y')
ax[2].axis('off')

plt.show()
