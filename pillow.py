#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 18:05:21 2018

@author: srikanth
"""

from PIL import Image,ImageFilter
myimage=Image.open('/home/srikanth/python/kaggledataset/bin_images/testingmodel/bin7')
myimage.load()
print(myimage.format,myimage.size,myimage.mode)
#blur the image
blurred=myimage.filter(ImageFilter.BLUR)
#save the new blur image
blurred.save('blur.png')
myimage.show()
blurred.show()
size=(100,100)
myimage.thumbnail(size)
myimage.show()
