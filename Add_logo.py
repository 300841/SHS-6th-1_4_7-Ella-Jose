import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw 

def add_logo(original_image, logo):
    '''adds a logo to the bottom right corner of all images'''
    