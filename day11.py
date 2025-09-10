import cv2

# a) Read an image and display it.
image = cv2.imread('new.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# b) Scale image by 1.5 and display it.
scaled_image_1 = cv2.resize(image, None, fx=1.5, fy=1.5)
cv2.imshow('Scaled Image (1.5)', scaled_image_1)
cv2.waitKey(0)

# c) Save above scaled image
cv2.imwrite('scaled_image_1.jpg', scaled_image_1)

# d) Scale original image – fx: 1.25, fy: 0.75 and display it.
scaled_image_2 = cv2.resize(image, None, fx=1.25, fy=0.75)
cv2.imshow('Scaled Image (1.25, 0.75)', scaled_image_2)
cv2.waitKey(0)

# e) Save above scaled image
cv2.imwrite('scaled_image_2.jpg', scaled_image_2)

# f) Change original image size to (300, 300) and display it.
resized_image = cv2.resize(image, (300, 300))
cv2.imshow('Resized Image (300x300)', resized_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
