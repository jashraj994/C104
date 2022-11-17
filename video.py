import cv2
img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
img[0:240,500:600]=rocket

text_show = "JASHRAJ SINGH" 
cv2.putText(img,text_show,(20,200),
fontFace = cv2.FONT_ITALIC,
fontScale = 1.5,
color=(0,0,255)

)

cv2.imshow("displayImage",img)
print(img)
cv2.waitKey(0)