import cv2

gambar = cv2.imread('ronaldo.jpg')

cv2.imshow("Ronaldo", gambar)

cv2.waitKey(0)
cv2.destroyAllWindows()