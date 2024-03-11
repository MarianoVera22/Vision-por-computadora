# Considerando los pasos detallados a continuación, realizar una alineación entre imágenes como se ejemplifica en las figuras 3 a la 6.
# 	- Capturar dos imágenes con diferentes vistas del mismo objeto
# 	- Computar puntos de interés y descriptores en ambas imágenes
# 	- Establecer matches entre ambos conjuntos de descriptores
# 	- Eliminar matches usando criterio de Lowe
# 	- Computar una homografía entre un conjunto de puntos y el otro
# 	- Aplicar la homografía sobre una de las imágenes y guardarla en otra (mezclarla con
# 	un alpha de 50 %)

import cv2
import numpy as np

MIN_MATCH_COUNT = 10

img1 = cv2.imread('imagen3.jpg')  # Leemos imagen 1
img2 = cv2.imread('imagen2.jpg')  # Leemos imagen 2
img1Copia = img1.copy()
img2Copia = img2.copy()

# Inicialización del detector y el descriptor
dscr = cv2.xfeatures2d.SIFT_create(100)

# Encontramos los puntos clave y los descriptores con SIFT en img1
kp1, des1 = dscr.detectAndCompute(img1, None)
# Encontramos los puntos clave y los descriptores con SIFT en img2
kp2, des2 = dscr.detectAndCompute(img2, None)

# Puntos claves
cv2.drawKeypoints(img1, kp1, img1Copia, (0, 255, 0))
cv2.drawKeypoints(img2, kp2, img2Copia, (0, 255, 0))
img_concatenate = np.concatenate(
    (img1Copia, img2Copia), axis=1)  # Concatenamos verticalmente
cv2.namedWindow('Puntos clave de las imagenes', cv2.WINDOW_NORMAL)
cv2.imshow('Puntos clave de las imagenes', img_concatenate)
cv2.imwrite('Puntos_clave.jpg', img_concatenate)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Matches
matcher = cv2.BFMatcher(cv2.NORM_L2)
matches = matcher.knnMatch(des1, des2, k=2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = []
total = []
for m, n in matches:
    total.append(m)
    if m.distance < 0.7*n.distance:
        good.append(m)

if(len(good) > MIN_MATCH_COUNT):
    scr_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # Computamos la homografía con RANSAC
    H, mask = cv2.findHomography(dst_pts, scr_pts, cv2.RANSAC, 5.0)

# Aplicamos la transformación perspectiva H a img2
wimg2 = cv2.warpPerspective(img2, H, img2.shape[:2][::-1])

# Gráfica de matches antes de Lowe
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, total, None)
cv2.namedWindow('Matches antes de Lowe', cv2.WINDOW_NORMAL)
cv2.imshow('Matches antes de Lowe', img_matches)
cv2.imwrite('Matches_sin_Lowe.jpg', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gráfica de matches despues de Lowe
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good, None)
cv2.namedWindow('Matches despues de Lowe', cv2.WINDOW_NORMAL)
cv2.imshow('Matches despues de Lowe', img_matches)
cv2.imwrite('Matches_con_Lowe.jpg', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2*alpha + img1*(1-alpha), dtype=np.uint8)
cv2.namedWindow('Imagen de salida', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen de salida', blend)
cv2.imwrite('Imagen_mezcla.jpg', blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
