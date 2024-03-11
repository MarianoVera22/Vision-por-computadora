# Teniendo en cuenta que:
#   - Una homografía se representa con una matriz de 3 × 3 (pero tiene sólo 8 grados de
#   libertad) y
#   - puede ser recuperada con 4 puntos no colineales.

# A. Crear una función que compute la homografía entre los 4 pares de puntos correspondientes.
# B. Usando como base el programa anterior, escriba un programa que
#   con la letra “h” permita seleccionar con el mouse 4 puntos no colineales en una
#   imagen y transforme (rectifique) la selección en una nueva imagen rectangular.

# Ayuda
#   - cv2.getPerspectiveTransform
#   - cv2.warpPerspective

import cv2
import numpy as np


def funcionRectificacion(img_orig):
    ax = []
    ay = []

    def img(event, x, y, flags, param):
        if(event == cv2.EVENT_LBUTTONDOWN and len(ax) < 4):

            cv2.line(img_orig, (x, y), (x, y), (255, 0, 0), 5)
            ax.append(x)
            ay.append(y)

    cv2.namedWindow('ImagenOrig')
    cv2.setMouseCallback('ImagenOrig', img)

    img_matriz = np.array(img_orig)

    print('Se debe seleccionar 4 puntos en sentido antihorario y empezando por el margen superior izquierdo')

    while(True):

        cv2.imshow('ImagenOrig', img_orig)
        cv2.waitKey(1)

        if(len(ax) == 4):

            scr = np.float32([[ax[0], ay[0]], [ax[1], ay[1]],
                             [ax[2], ay[2]], [ax[3], ay[3]]])

            AnchoSup = np.sqrt(((ax[0] - ax[3]) ** 2) + ((ay[0] - ay[3]) ** 2))
            AnchoInf = np.sqrt(((ax[1] - ax[2]) ** 2) + ((ay[1] - ay[2]) ** 2))
            Ancho = max(int(AnchoSup), int(AnchoInf))

            AltoIzq = np.sqrt(((ax[0] - ax[1]) ** 2) + ((ay[0] - ay[1]) ** 2))
            AltoDer = np.sqrt(((ax[2] - ax[3]) ** 2) + ((ay[2] - ay[3]) ** 2))
            Alto = max(int(AltoIzq), int(AltoDer))

            dst = np.float32(
                [[0, 0], [0, Alto - 1], [Ancho - 1, Alto - 1], [Ancho - 1, 0]])

            M = cv2.getPerspectiveTransform(scr, dst)

            img_perp = cv2.warpPerspective(
                img_matriz, M, (Ancho, Alto), flags=cv2.INTER_LINEAR)

            cv2.imwrite('imagenRectificada.jpg', img_perp)

            k = cv2.waitKey(1) & 0xFF
            cv2.imshow('imagenRectificada', img_perp)

            if(k == ord('q')):
                cv2.destroyWindow('imagenRectificada')
                break
