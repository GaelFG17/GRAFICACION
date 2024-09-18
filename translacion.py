from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Abre la imagen
imagen = Image.open('imagen.jpg')

# Desplazamiento (translación)
t_x = 30  # Traslación en x
t_y = 50  # Traslación en y

# Matriz de translación
matriz_translacion = np.array([
    [1, 0, t_x],
    [0, 1, t_y],
    [0, 0, 1]
])

ancho, alto = imagen.size

# Crear una nueva imagen para aplicar la translación
nueva_img = Image.new('RGB', (ancho, alto))

# Aplicar la translación
for x in range(ancho):
    for y in range(alto):
        # Crear el vector de coordenadas homogéneas
        coord = np.array([x, y, 1])

        # Aplicar la matriz de translación
        nueva_coord = np.dot(matriz_translacion, coord)

        # Obtener las nuevas coordenadas trasladadas
        x_trasl = int(nueva_coord[0])
        y_trasl = int(nueva_coord[1])

        # Comprobar si las nuevas coordenadas están dentro de los límites de la imagen
        if 0 <= x_trasl < ancho and 0 <= y_trasl < alto:
            # Copiar el píxel original a la nueva ubicación
            nueva_img.putpixel((x_trasl, y_trasl), imagen.getpixel((x, y)))

# Convertir las imágenes a arreglos numpy para graficar
original_img_array = np.array(imagen)
transladada_img_array = np.array(nueva_img)

# Graficar la imagen original y la trasladada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Mostrar la imagen original
axes[0].imshow(original_img_array)
axes[0].set_title('Imagen Original')
axes[0].axis('off')  # Quitar los ejes

# Mostrar la imagen trasladada
axes[1].imshow(transladada_img_array)
axes[1].set_title('Imagen Translacionada')
axes[1].axis('off')  # Quitar los ejes

# Mostrar las gráficas
plt.show()