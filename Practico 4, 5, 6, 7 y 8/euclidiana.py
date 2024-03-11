# A) Crear una función que aplique una transformación euclidiana, recibiendo los siguientes parámetros:
# 		Parámetros
# 			• angle: Ángulo
# 			• tx: traslación en x
# 			• ty: traslación en y

# 		Recordar que la transformación euclidiana tiene la siguiente forma:
# 			[ cos(angle)	sin(angle)		tx ]
# 			[ -sin(angle)	cos(angle) 		ty ]

# B) Escribir un programa que permita seleccionar
# 	una porción rectangular de una imagen y
# 		- Con la letra “e” aplique una transformación euclidiana a la porción de imagen
# 		seleccionada y la guarde como una nueva imagen.

import cv2
import numpy as np


def funcionEuclidiana(x, y, ang, imagen):
    (ht, wt) = (imagen.shape[0], imagen.shape[1])

    Mt = np.float32([[1, 0, x], [0, 1, y]])  # Matriz traslación
    desplazada = cv2.warpAffine(imagen, Mt, (wt, ht))

    centro = None
    if centro is None:
        centro = (wt/2, ht/2)

    (hr, wr) = desplazada.shape[:2]
    Mr = cv2.getRotationMatrix2D(centro, ang, 1)  # Matriz rotación
    rotada = cv2.warpAffine(desplazada, Mr, (hr, wr))

    return rotada
