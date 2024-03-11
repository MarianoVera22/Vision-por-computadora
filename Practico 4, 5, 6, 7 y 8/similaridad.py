# A) Agregar a la función anterior un parámetro que permita aplicar un escalado a la porción rectangular de imagen.
# 	Parámetros
# 		• angle: Ángulo
# 		• tx: traslación en x
# 		• ty: traslación en y
# 		• s: escala

# 	Recordar que la transformación de similaridad tiene la siguiente forma:
# 		[ s.cos(angle)		s.sin(angle)	tx ]
# 		[ -s.sin(angle) 	s.cos(angle)	ty ]

# B) Escribir un programa que permita seleccionar una porción rectangular de una imagen y
# 	- Con la letra “s” aplique una transformación de similaridad a la porción de imagen
# 	seleccionada y la guarde como una nueva imagen.

import cv2
import numpy as np


def funcionSimilaridad(x, y, ang, imagen, s):
    (ht, wt) = (imagen.shape[0], imagen.shape[1])

    Mt = np.float32([[1, 0, x], [0, 1, y]])  # Matriz traslación
    desplazada = cv2.warpAffine(imagen, Mt, (wt, ht))

    centro = None
    if centro is None:
        centro = (wt/2, ht/2)

    (hr, wr) = desplazada.shape[:2]
    # Matriz rotación con escalado
    Mr = cv2.getRotationMatrix2D(centro, ang, s)
    rotada = cv2.warpAffine(desplazada, Mr, (hr, wr))

    return rotada
