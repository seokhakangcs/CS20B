"""
hjgjhgjh
"""
from PIL import Image, ImageFilter, ImageEnhance

image = Image.open("/Users/kang/Documents/CS20B/dog.jpg")

"""
1. Rotate the image by 50 degrees.
2. Blur the image.
3. Make the image transparent.
4. Control the contrast.
"""
image.show()
rotateImage = image.rotate(50)
blurred = rotateImage.filter(ImageFilter.BLUR)
blurred.putalpha(128)
imageEnhance = ImageEnhance.Contrast(blurred)

imageEnhance.enhance(5.0).show()
