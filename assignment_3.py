# from cImage import *
import image
# from tkinter import *


def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()
    newIm = image.EmptyImage(oldW * 2, oldH * 2)
    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col, row)
            newIm.setPixel(2 * col, 2 * row, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
            newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)
    return newIm


myImage = image.FileImage("/Users/kang/Documents/CS20B/download.jpeg")
height = myImage.getHeight()
width = myImage.getWidth()
print(height, width)
print(type(height))
myWin = image.ImageWin("Image_testing", width, height)
myImage.draw(myWin)
myWin.exit_on_click()
doubleImage(myImage)
