import cv2
import numpy as np
from kivy.app import App
from kivy.uix.image import Image,AsyncImage

from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance


class contrastAdjustment(App):
    def build(self):
        img = cv2.imread('vison.jpg')
        contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
        cv2.imshow('original image', img)
        cv2.imshow('contrast adjustmenr', contrast_img)
        cv2.waitKey(0)


contrastAdjustment().run()