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

    #since i am using the image module,i am having a hard time finding out how to reposition my rectangle on the mandelbrot,
    #since it appears that a lot of the x and y-values that make colors(not in mandelbrot-set) are decimals,
    #and i dont understand how i am going to apply these decimal-ranges to my coordinates,since my coordinates mostly
    #are positive from 0 and so on so i just
    #multiply with a decimal to scale the integers from for example min 0 to max 500 before i add it to the function
    #which finds out the iterations below in the mandelbrot. SO now, it appears
    #that the minX and maxY just decides the resolution of my image, which would work, if you think about it, to zoom in and explore
    #the pattern.
    #BUT ON THE BRIGHT SIDE: Although this might be a bad solution, it certainly takes a lot of computation, and it appears
    #that you(the instructors), made this task to focus on the computation of mandelbrot, and not the image, in this case, my solution
    #is adequate.

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
