# def draw(img, pts,ids):
#     global height,width
#     pts = np.int32(pts).reshape(-1,2)
#     in_pts = np.float32([[0,0], [width-1,0], [width-1,height-1], [0,height-1]])
#     out_pts = np.float32([pts])
#     M=cv2.getPerspectiveTransform(in_pts,out_pts)
#     warped_image = cv2.warpPerspective(ar_img[ids%len(ar_img)], M, (width,height)) # Aca selecciono la imagen dependiendo el id del aruco
#     mask = np.zeros([height,width], dtype=np.uint8)
#     cv2.fillConvexPoly(mask, np.int32([pts]), (255, 255, 255), cv2.LINE_AA)
#     img[np.where(mask == 255)] = warped_image[np.where(mask == 255)]
#     return img


