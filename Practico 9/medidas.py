# Como dato de entrada, sabemos que el tamaño del marco de la puerta es de 2.10m de
# alto por 0.73m de ancho. En base a estas medidas hacer un programa que permita medir el
# largo de cosas en el plano de la fachada.

# Capturar una imagen de una fachada con perspectiva y hacer un programa que permita:
#   - encontrar la transformación perspectiva entre los 4 vértices del marco y un rectángulo
#       con la misma relación de aspecto que la puerta real;
#   - aplicar dicha transformación a la imagen y mostrarla en una ventana;
#   - sobre esta ventana permitir que el usuario haga dos clicks y mostrar la distancia en
#       metros entre dichos puntos;
#   - permitir que cuando se presione la tecla “r” se reinicie la medición;
#   - por último medir dos objetos en la imagen (ventana, casilla del gas, etc.) y comparar
#       los resultados con la medida real.

import cv2
import numpy as np
import math


i = 0
x_e, y_e = [], []

# Coordenadas de la puerta en la imagen original con el script coord.py
puntos = np.float32([[1183, 193], [1183, 770], [982, 800], [979, 187]])

# 3----0
# |    |
# |    |
# 2----1
x_d = puntos[0, 0] - 300
y_d = puntos[0, 1]

# Longitudes en pixels
p_ancho = puntos[2, 0] - puntos[0, 0]
p_alto = puntos[3, 1] - puntos[2, 1]

# Puerta: 2.06m x 0.82m
# Relacion de distancias entre cm y pixels
r_alto = 206 / p_alto
r_ancho = 82 / p_ancho

# Puntos de destino del mapeo
destino = np.float32([[x_d, y_d], [x_d, (y_d - p_alto)],
                     [(x_d + p_ancho), (y_d - p_alto)], [(x_d + p_ancho), y_d]])

# Transformación prespectiva
def prespectiva(imagen, puntos, destino):
    (h, w) = imagen.shape[:2]
    trans = cv2.getPerspectiveTransform(puntos, destino)
    presp = cv2.warpPerspective(imagen, trans, (h, w - 300))
    return presp

# Cálculo de distancia
def calculoDist(event, x, y, flag, params):
    global i, x_e, y_e, dist, img_presp
    if event == cv2.EVENT_LBUTTONDOWN:
        if i < 2:
            cv2.circle(img_presp, (x, y), 4, (0, 0, 255), -1)
            cv2.imshow('Imagen en prespectiva', img_presp)
        if i == 0:
            x_e.append(x)
            y_e.append(y)
        if i == 1:
            x_e.append(x)
            y_e.append(y)
            dist = np.float32(math.sqrt(((x_e[1]-x_e[0])*r_ancho)
                              ** 2 + ((y_e[1]-y_e[0]) * r_alto)**2))
            print("\nDistancia: ", dist, "cm")
        i += 1

        if i == 2:
            img_presp = cv2.line(
                img_presp, (x_e[0], y_e[0]), (x_e[1], y_e[1]), (0, 255, 0), 1)

            cv2.putText(img_presp, str(dist)+" cm", (int((x_e[0]+x_e[1])/2), int(
                (y_e[0]+y_e[1])/2)), cv2.FONT_ITALIC, 1, (0, 255, 0), 1, cv2.LINE_AA)
            x_e = []
            y_e = []
            cv2.imshow('Imagen en prespectiva', img_presp)
            cv2.setMouseCallback('Imagen en prespectiva', eventOff)

# Suspende eventos del mouse
def eventOff(event, x, y, flag, params):
    event == cv2.EVENT_LBUTTONDOWN
    event == cv2.EVENT_LBUTTONUP


img_orig = cv2.imread('entrada.jpg', 1)
img_presp = prespectiva(img_orig, puntos, destino)
(h, w) = img_orig.shape[:2]
img_copia = img_presp.copy()

cv2.imshow('Imagen Original', img_orig)
cv2.waitKey(100)

cv2.namedWindow('Imagen en prespectiva')
(h, w) = img_presp.shape[:2]

cv2.imshow('Imagen en prespectiva', img_presp)
print("M/R - Medir/Restaurar\nQ - Salir")

cv2.setMouseCallback('Imagen en prespectiva', eventOff)

while(1):

    k = cv2.waitKey(100) & 0xFF

    if k == ord('m'):      # mide distancia entre dos puntos seleccionados, tambien lo uso para reiniciar medicion
        img_presp = img_copia.copy()
        cv2.imshow('Imagen en prespectiva', img_presp)
        i = 0
        cv2.setMouseCallback('Imagen en prespectiva', calculoDist)

    elif k == ord('r'):     # idem opcion m
        img_presp = img_copia.copy()
        cv2.imshow('Imagen en prespectiva', img_presp)
        i = 0
        cv2.setMouseCallback('Imagen en prespectiva', calculoDist)

    elif k == ord('q'):  # q sale del programa
        break

cv2.destroyAllWindows()
