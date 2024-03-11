# Teniendo en cuenta que:
#   - Una transformación afín se representa con una matriz de 2 × 3 (tiene 6 grados de libertad) y
#   - Puede ser recuperada con 3 puntos no colineales.

# A. Crear una función que compute la transformación afín entre 3 pares de puntos correspondientes.
# B. Usando como base el programa anterior, escriba un programa que
#   con la letra “a” permita seleccionar con el mouse 3 puntos no colineales en una
#   imagen e incruste entre estos puntos seleccionados una segunda imagen.

# Ayuda
#   - cv2.getAffineTransform
#   - cv2.warpAffine
#   - Generar una máscara para insertar una imagen en otra


import numpy as np
import cv2


def funcionAfin(imagen):
    ax = []
    ay = []

    def img(event, x, y, flags, param):
        if(event == cv2.EVENT_LBUTTONDOWN and len(ax) < 3):

            cv2.line(imagen, (x, y), (x, y), (255, 0, 0), 5)
            ax.append(x)
            ay.append(y)

        elif(event == cv2.EVENT_LBUTTONUP and len(ax) == 3):

            scr = cv2.imread('gaston.png')

            srcTri = np.float32([[0, 0], [scr.shape[1], 0], [
                                scr.shape[1], scr.shape[0]]])
            dstTri = np.float32(
                [[ax[0], ay[0]], [ax[1], ay[1]], [ax[2], ay[2]]])

            warp_mat = cv2.getAffineTransform(srcTri, dstTri)
            warp_dst = cv2.warpAffine(
                scr, warp_mat, (imagen.shape[1], imagen.shape[0]))

            mascara = np.zeros(
                [imagen.shape[0], imagen.shape[1], imagen.shape[2]], np.uint8)

            for i, row in enumerate(warp_dst):
                for j, col in enumerate(row):
                    if(col[0] == 0 and col[1] == 0 and col[2] == 0):
                        mascara[i, j, :] = 1

            imgAux = (mascara) * imagen

            imagenTotal = imgAux + warp_dst

            cv2.imwrite('imagenAfin.jpg', imagenTotal)
            cv2.imshow('ImagenModificada', imagenTotal)
            cv2.waitKey(0)
            cv2.destroyWindow('ImagenModificada')
            print("q para salir")

    cv2.namedWindow('imagenAfin')
    cv2.setMouseCallback('imagenAfin', img)

    while(True):

        cv2.imshow('imagenAfin', imagen)

        k = cv2.waitKey(1) & 0xFF

        if(k == ord('q')):  # Volver
            cv2.destroyWindow('imagenAfin')
            break
