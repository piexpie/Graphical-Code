import numpy

data = numpy.zeros((100, 100, 3), dtype=numpy.uint8)

data[50,50] = [255, 0, 0]
data[50,50] = [0, 255, 0]
data[50,50] = [0, 0, 255]

white = [255,255,255]

for i in range(0, 100):
    if (i%2 == 0):
        data[i,50] = white
        data[50,i] = white
        data[i,i] = white
        data[-i,i] = white

from PIL import Image

image = Image.fromarray(data)

image.show()