
import sys
from PIL import Image
from PIL import ImageDraw
from random import randint
import time
import numpy as np





#threshold = 1000
def compute_mandelbrot(c):

    z = complex(0,0)
    #we iterate a given amount(threshold), and check if our c is in the mandelbrot
    for i in np.arange(0,1000):

        z = z*z+c
        #if our absolute value of z, which is run a given amount of times over itself, is
        #ever over 2, we know that it has escaped our escape value of 2, and is in the mandelbrot set
        #which is only when z can be added many times together for the value of c(complex coordinate)
        #and never goes over 2.
        #If c is not n the mandelbrot set, we return how many times we iterated before the c escaped 2

        if(abs(z)>2):
            return i

    #np.absolute(array)

    #if our z never goes over 2, we know its in the mandelbrot set, and its coordinates will be painted black
    #we fix the coloring later
    return None;

#returns color vector based on x and y coordinate, also maxX and minX in order to scale, and a colormap ofcourse
def getColorVector(colormap,maxX,minX,x,y,centerX,centerY):

    scaleFix=1.0/((maxX-minX)/3)

    #optimal center = (2.2,1.5)
    center=(centerX,centerY)

    iterations = compute_mandelbrot(complex(x*scaleFix-center[0],y*scaleFix-center[1]))

    if(iterations == None):
        return [0,0,0]

    return colormap[iterations]

#function that use numpy for the solving
def makeMandelbrotImageNumpy(minX,maxX,minY,maxY,centerX,centerY,colorStyle,fileName):

    width = maxX-minX
    height = maxY-minY

    #make array with our grid in numpy
    gridNumpy = np.ones((height,width,3),dtype=np.uint8)






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


    #hopefully the following code would have worked, so that i would have been aple to compute all colors on the whole array
    #of x and y coordinates at the same time with numpy, to find my rbg value(with the getColorVector method), and then add it to the corresponding
    #x and y coordinate as a value. Python doesnt seem to want to add the tuple of (r,b,g) as a value in the 2d array,
    #and i cant seem to find out how to do this. Therefore this implementation is just as slow as the first one.

    #a = np.zeros((width,height),dtype=(float,3))
    #func=np.vectorize(getColorVector)
    #a=np.fromfunction(func,(colorCollection,maxX,minX,range(0,width),range(0,height)))



            gridNumpy = gridNUmpy*getColorVector(colorCollection,maxX,minX,2,3,centerX,centerY)


    image = Image.fromarray(gridNumpy,'RGB')
    image.save(fileName)


#make mandelbrot with minX=0,maxX=1000,minY=0;maxY=1000, and filename



#startTime = time.time();
#makeMandelbrotImageNumpy(0,200,0,200,"result2.png")
#endTime = time.time();

#total = endTime-startTime;

#print(total);
