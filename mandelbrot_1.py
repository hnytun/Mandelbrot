from PIL import Image
from PIL import ImageDraw
from random import randint
import time
import numpy as np


#compute mandelbrot
#threshold = 1000
def compute_mandelbrot(c):

    z = complex(0,0)
    #we iterate a given amount(threshold), and check if our c is in the mandelbrot
    for i in range(0,1000):
        z = z*z+c
        #if our absolute value of z, which is run a given amount of times over itself, is
        #ever over 2, we know that it has escaped our escape value of 2, and is not in the mandelbrot set
        #which is only when z can be added many times together for the value of c(complex coordinate)
        #and never goes over 2.
        #If c is not n the mandelbrot set, we return how many times we iterated before the c escaped 2
        if(abs(z)>2):
            return i
    #if our z never goes over 2, we know its in the mandelbrot set, and its coordinates will be painted black
    #we fix the coloring later
    return None;

#function that doesnt use numpy for the solving
def makeMandelbrotImageTraditional(minX,maxX,minY,maxY,centerX,centerY,colorStyle,fileName):
    #add 1000 colors to our grid depending on what scale we are following (colorstyle)
    if(colorStyle == "random"):
        colorCollection = np.random.randint(255,size=(1000,3))
    elif(colorStyle == "red"):#alternative color1 red
        colorCollection = [0]*1000
        for i in range (0,1000):
            while True:
                r=randint(0,255)
                g=randint(0,20)
                b=randint(0,20)

                if (r,g,b) not in colorCollection: #in order to create distinct colors
                    break
                #if the color is not in our list yet we break and end up here
            colorCollection[i] = (r,g,b)
    elif(colorStyle=="blue"):   #alternative color2 blue
        colorCollection = [0]*1000
        for i in range (0,1000):

            while True:
                r=randint(0,255)
                g=randint(94,255)
                b=randint(250,255)

                if (r,g,b) not in colorCollection: #in order to create distinct colors
                    break
        #if the color is not in our list yet we break and end up here
            colorCollection[i] = (r,g,b)
    elif(colorStyle=="purple"):#alternative color3 purp
        colorCollection = [0]*1000

        for i in range (0,1000):

            while True:
                r=randint(0,255)
                g=randint(0,5)
                b=randint(0,230)

                if (r,g,b) not in colorCollection: #in order to create distinct colors
                    break
        #if the color is not in our list yet we break and end up here
            colorCollection[i] = (r,g,b)

    #rectangle to be filled, change from 0 to 1000 in min and max to get full picture. I dont really understand how to do this task
    #in another way
    scaleFix=1.0/((maxX-minX)/3)

    #uncomment bottom center initialization to make center 0, but this makes the pattern more boring
    #center=(2.2,1.5)
    #center =(0.0,0.0)

    image = Image.new("RGB",(maxX-minX,maxY-minY))
    drawer = ImageDraw.Draw(image)
    #colorize our rectangle
    for x in range (minX,maxX):
        for y in range (minY,maxY):
            iterationsBeforeEscape = compute_mandelbrot(complex(x*scaleFix-centerX,y*scaleFix-centerY))
            if(iterationsBeforeEscape == None):
                drawer.point((x,y),fill = (0,0,0))
            else:
                drawer.point((x,y),fill = colorCollection[iterationsBeforeEscape])

    image.save(fileName)

#make mandelbrot with minX=0,maxX=1000,minY=0;maxY=1000, and filename
#startTime = time.time();
makeMandelbrotImageTraditional(0,200,0,200,"result1.png")
#endTime = time.time();
#total = endTime-startTime;
#print(total);




















#
