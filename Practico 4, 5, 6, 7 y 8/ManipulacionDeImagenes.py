# Escribir un programa que permita seleccionar
# una porción rectangular de una imagen

import cv2
from cv2 import imshow
import numpy as np
import euclidiana
import similaridad
import afin
import rectificacion


drawing = False
rectangulo = 0

img = cv2.imread('hoja.png')
imgCopia = np.array(img)
u_ix, u_iy = -1, -1
d_ix, d_iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global u_ix, u_iy, d_ix, d_iy, drawing, mode, rectangulo, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        u_ix, u_iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = np.array(imgCopia)
            d_ix, d_iy = x, y
            cv2.rectangle(img, (u_ix, u_iy), (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangulo = 1


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
imgCopia = np.array(img)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    #   - Con la letra “g” guardar la porción de la imagen seleccionada como una nueva
    #     imagen,
    if k == ord('g'):
        if (rectangulo == 1):
            imgRecortada = imgCopia[u_iy: d_iy, u_ix: d_ix]
            cv2.imwrite('imagenRecortada.png', imgRecortada)
        else:
            print('No hay rectangulo seleccionado')

    # 	- Con la letra “e” aplique una transformación euclidiana a la porción de imagen
    # 	  seleccionada y la guarde como una nueva imagen.
    elif k == ord('e'):
        if (rectangulo == 1):
            imgRecortada = imgCopia[u_iy: d_iy, u_ix: d_ix]
            x_e = int(input("Cantidad en x: "))
            y_e = int(input("Cantidad en y: "))
            angulo_e = int(input("Cantidad de angulo: "))
            imgEuclidiana = euclidiana.funcionEuclidiana(
                x_e, y_e, angulo_e, imgRecortada)
            cv2.imwrite('imagenEuclidiana.png', imgEuclidiana)
        else:
            print('No hay rectangulo seleccionado')

    #   - Con la letra “s” aplique una transformación de similaridad a la porción de imagen
    #     seleccionada y la guarde como una nueva imagen.
    elif k == ord('s'):
        if (rectangulo == 1):
            imgRecortada = imgCopia[u_iy: d_iy, u_ix: d_ix]
            x_s = int(input("Cantidad en x: "))
            y_s = int(input("Cantidad en y: "))
            angulo_s = int(input("Cantidad de angulo: "))
            s_s = float(input("Cantidad de escalado: "))
            imgSimilaridad = similaridad.funcionSimilaridad(
                x_s, y_s, angulo_s, imgRecortada, s_s)
            cv2.imwrite('imagenSimiliridad.png', imgSimilaridad)
        else:
            print('No hay rectangulo seleccionado')

    #   B.Escriba un programa que
    #   con la letra “a” permita seleccionar con el mouse 3 puntos no colineales en una
    #   imagen e incruste entre estos puntos seleccionados una segunda imagen.
    elif(k == ord('a')):
        cv2.destroyWindow('image')
        imgOriginal = cv2.imread('hoja.png')
        imgAfin = afin.funcionAfin(imgOriginal)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_circle)

    #   - Con la letra “r” restaurar la imagen original y permitir realizar una nueva selección,
    elif k == ord('r'):
        img = np.array(imgCopia)
        rectangulo = 0

    #   Escriba un programa que
    #   con la letra “h” permita seleccionar con el mouse 4 puntos no colineales en una
    #   imagen y transforme (rectifique) la selección en una nueva imagen rectangular.
    if(k == ord('h')):
        cv2.destroyWindow('image')
        imgOriginal = cv2.imread('gabinete.jpg')
        imgRectificada = rectificacion.funcionRectificacion(imgOriginal)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_circle)
        cv2.destroyWindow('ImagenOrig')

    #   - Con la “q” finalizar.
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
