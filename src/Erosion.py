import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
filename = 'vison.jpg'
image = Image.open(filename)
size = width, height = image.size

input_image = cv2.imread('vison.jpg', cv2.IMREAD_COLOR)
kernel = np.ones((5,5), np.uint8)
erosion_image = cv2.erode(input_image, kernel, iterations=1)
cv2.imshow('Input', input_image)
cv2.imshow('Erosion', erosion_image)

cv2.waitKey(0)

