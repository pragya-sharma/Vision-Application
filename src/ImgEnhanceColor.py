import cv2
import numpy as np
from kivy.app import App
from kivy.uix.image import Image,AsyncImage

from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance


class imgEnhanceColor(App):
    filename = 'vison.jpg'
    image = Image.open(filename)
    size = width, height = image.size

    enhancer = ImageEnhance.Color(image)
    # if we give 0.0 then it will inhance in white and black
    image = enhancer.enhance(0.5)

    image.save('modifi' + filename)
    image.show()

imgEnhanceColor().run()