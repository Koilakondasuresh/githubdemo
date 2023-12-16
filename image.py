import cv2
#read the image
img=cv2.imread("s.jpg")
#image show
cv2.imshow('image',img)
cv2.waitKey(5000)

print(img.shape)
print(img.size)
print(img.dtype)
cv2.destroyAllWindows()