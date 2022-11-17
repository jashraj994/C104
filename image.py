import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("displayImage",img)
print(img)
greyImage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("greyImage",greyImage)
print(greyImage)
cv2.waitKey(0)