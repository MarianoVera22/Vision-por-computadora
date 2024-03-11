#! /usr/bin/env python
# -*-coding: utf-8-*-

# A. ¿Cómo obtener el frame rate o fps usando las OpenCV?
# Usarlo para no tener que harcodear el delay del waitKey.

# B. ¿Cómo obtener el ancho y alto de las imágenes capturadas usando las OpenCV? Usarlo
# para no tener que harcodear el frameSize del video generado.


import sys
import cv2

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print("Pasar el nombre de archivo como argumento")
    sys.exit(0)

cap = cv2.VideoCapture('comiendo.mp4')  # Captura el video
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# FourCC (Four Characters Code) es un código que utiliza 4 caracteres (letras o números) con que se identifica cada códec.
# Ejemplos:
#   XVID = Xvid
#   DX50 = DivX
#   Dirac = drac

# framesize=(680,480)
alto = int(cap.get(3))  # CAP_PROP_FRAME_WIDTH
ancho = int(cap.get(4))  # CAP_PROP_FRAME_HEIGHT
framesize = (alto, ancho)
print('Framesize: {}'.format(framesize))

out = cv2.VideoWriter('output.avi', fourcc, 20.0, framesize)

# delay=33
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS: {}".format(fps))
delay = int(round((1/round(fps))*1000)-1)
print("Delay: {}".format(delay))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        window_name = 'Imagen'
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow(window_name, gray)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
