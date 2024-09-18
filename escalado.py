from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Abre la imagen
imagen = Image.open('imagen.jpg')

# Factores de escalado
s_x = 0.5  
s_y = 0.7  

# Convertir imagen a matriz de píxeles
pixeles = np.array(imagen)

# Obtener el tamaño original
alto, ancho, canales = pixeles.shape

# Calcular el nuevo tamaño
nuevo_ancho = int(ancho * s_x)
nuevo_alto = int(alto * s_y)

# Crear una nueva matriz para los píxeles escalados
nueva_img = np.zeros((nuevo_alto, nuevo_ancho, canales), dtype=np.uint8)

# Matriz de escalado
matriz_escalado = np.array([
    [s_x, 0, 0],
    [0, s_y, 0],
    [0, 0, 1]
])

# Calcular la inversa de la matriz de escalado para transformar de nuevo a coordenadas originales
matriz_inversa = np.linalg.inv(matriz_escalado)

# Aplicar escalado a cada píxel
for y in range(nuevo_alto):
    for x in range(nuevo_ancho):
        # Crear el vector de coordenadas homogéneas para la nueva imagen
        coord_nueva = np.array([x, y, 1])

        
        coord_original = np.dot(matriz_inversa, coord_nueva)
        
        
        x_orig = int(coord_original[0])
        y_orig = int(coord_original[1])

        
        x_orig = min(max(x_orig, 0), ancho - 1)
        y_orig = min(max(y_orig, 0), alto - 1)

        
        nueva_img[y, x] = pixeles[y_orig, x_orig]

# Convertir la matriz de nuevo a una imagen PIL
nueva_img_pil = Image.fromarray(nueva_img)

# Guardar la nueva imagen escalada
nueva_img_pil.save('imagen_escalada.jpg')
