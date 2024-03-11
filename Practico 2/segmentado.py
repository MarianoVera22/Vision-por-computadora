# Escribir un programa en python que lea una imagen y realice un umbralizado binario,
# guardando el resultado en otra imagen.
#  - NOTA: No usar ninguna función de las OpenCV, excepto para leer y guardar la
#    imagen.

import cv2

img = cv2.imread("hoja.png", 0)  # Dejo la imagen en escala de grises
cv2.imwrite("salida2.png", img)

x, y = img.shape  # Carga los indices de la matriz imagen en x e y respectivamente
print(x, y)
limite = 200

for i in range(x):  # Recorrido de filas
    for j in range(y):  # Recorrido de columnas
        if(img[i, j] < limite):
            img[i, j] = 0  # Poner en negro el pixel
        else:
            img[i, j] = 255  # Poner en blanco el pixel

cv2.imwrite("resultado.png", img)
