
import sys
from PIL import Image
from PIL import ImageDraw
from random import randint
import time
import numpy as np
import mandelbrot_1
import mandelbrot_2
#import mandelbrot_3






if sys.argv[1] == "--help":
    print("|---------------------------------------------------------------------------------------------------|")
    print("|                                                                                                   |")
    print("|    format for running scripts: mandelbrot[version] minX maxX minY maxY centerX centerY colorstyle filename   |")
    print("     you can change centerX and centerY to change where the rectangle from minX to maxX and minY to maxY is ")
    print("|    NOTE: for optimal position on image enter 2.2 for centerX and 1.5 for centerY                 |")
    print("|            versions = mandelbrot1,mandelbrot2,mandelbrot3(NOT FINISHED)                           |")
    print("                      AVAILABLE COLORSTYLES=RED,BLUE,PURPLE AND NORMAL                               ")
    print("|                                                                                                   |")
    print("|---------------------------------------------------------------------------------------------------|")
elif sys.argv[1] == "mandelbrot1":
    minX = sys.argv[2]
    maxX = sys.argv[3]
    minY = sys.argv[4]
    maxY = sys.argv[5]
    centerX = sys.argv[6]
    centerY = sys.argv[7]
    colorstyle = sys.argv[8]
    filename = sys.argv[9]
    mandelbrot_1.makeMandelbrotImageTraditional(int(minX),int(maxX),int(minY),int(maxY),float(centerX),float(centerY),colorstyle,filename)
elif sys.argv[1] == "mandelbrot2":
    minX = sys.argv[2]
    maxX = sys.argv[3]
    minY = sys.argv[4]
    maxY = sys.argv[5]
    centerX = sys.argv[6]
    centerY = sys.argv[7]
    colorstyle = sys.argv[8]
    filename = sys.argv[9]
    mandelbrot_2.makeMandelbrotImageNumpy(int(minX),int(maxX),int(minY),int(maxY),float(centerX),float(centerY),colorstyle,filename)
elif sys.argv[1] == "mandelbrot3":
    print("not finished")
