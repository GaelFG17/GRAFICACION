from PIL import Image
import numpy as np
import math
from matplotlib import pyplot as plt

# Abre la imagen
imagen = Image.open('imagen.jpg')

angulo = 180
angulo_rad = math.radians(angulo)
#formula matricial
matriz_rot = [
    [math.cos(angulo_rad),-math.sin(angulo_rad)],
    [math.sin(angulo_rad), math.cos(angulo_rad)]
]


ancho, alto = imagen.size

nueva_img = Image.new('RGB', (ancho,alto))

#Rotar imagen
for x in range(ancho):
    for y in range(alto):
        x_origen = x-ancho // 2
        y_origen = y-alto // 2
        
        x_rot = int(x_origen * matriz_rot[0][0] + y_origen * matriz_rot[0][1]) + ancho // 2
        y_rot = int(x_origen * matriz_rot[1][0] + y_origen * matriz_rot[1][1]) + alto // 2
    
    #comprobar 
        if 0 <= x_rot < ancho and 0 <= y_rot < alto:
            nueva_img.putpixel(((x_rot), int(y_rot)), imagen.getpixel((x, y)))

    
nueva_img.save('imagenRotada.jpg')    
        