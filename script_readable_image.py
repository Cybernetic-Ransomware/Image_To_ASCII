import cv2


img = cv2.imread('input_images/post-46652-0-29904700-1483520804.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (600, 800))

_, result = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)

adaprive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 15)

cv2.imshow('title', result)
cv2.imshow('original', img)
cv2.imshow('adaptive', adaprive_result)
cv2.waitKey(0)
