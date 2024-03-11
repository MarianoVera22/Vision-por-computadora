import cv2
import numpy as np

parametros = cv2.aruco.DetectorParameters_create()

diccionario = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    esquinas, ids, candidatos_malos = cv2.aruco.detectMarkers(
        gray, diccionario, parameters=parametros)

    if np.all(ids != None):
        # for aruco_corner in esquinas:
        #     frame=draw(frame, aruco_corner)
        # if borders:
        #   aruco=cv2.aruco.drawDetectedMarkers(frame, esquinas)
        # cv2.imshow("Cubo rubik",frame)

        # corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        # if ids is not None:
        #   for i, my_id in enumerate(ids):
        #       frame = draw(frame,corners[i],my_id)

        # aruco.drawDetectedMarkers(frame, corners)
        # cv2.imshow("Image", frame)

        aruco = cv2.aruco.drawDetectedMarkers(frame, esquinas)

        c1 = (esquinas[0][0][0][0], esquinas[0][0][0][1])
        c2 = (esquinas[0][0][1][0], esquinas[0][0][1][1])
        c3 = (esquinas[0][0][2][0], esquinas[0][0][2][1])
        c4 = (esquinas[0][0][3][0], esquinas[0][0][3][1])

        copy = frame
        imagen = cv2.imread("imagen1.png")
        tam = imagen.shape
        puntos_aruco = np.array([c1, c2, c3, c4])
        puntos_imagen = np.array(
            [[0, 0], [tam[1]-1, 0], [tam[1]-1, tam[0]-1], [0, tam[0]-1]], dtype=float)

        h, estado = cv2.findHomography(puntos_imagen, puntos_aruco)

        perspectiva = cv2.warpPerspective(
            imagen, h, (copy.shape[1], copy.shape[0]))
        cv2.fillConvexPoly(copy, puntos_aruco.astype(int), 0, 16)
        copy = copy+perspectiva
        cv2.imshow("Cubo rubik", copy)

    else:
        cv2.imshow("Cubo rubik", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
