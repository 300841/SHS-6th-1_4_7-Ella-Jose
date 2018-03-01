import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw 

def add_frame(original_image, percent_of_side=.3, image):
    '''adds a frame to all images'''
    