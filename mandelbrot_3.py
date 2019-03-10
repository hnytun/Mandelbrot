import pyximport; pyximport.install()
import mandelbrot_3
import numpy as np



a=np.ones(100,dtype=np.int64)

sum = mandelbrot_3.sum_np(a)

mandelbrot_3.calculateMandelBrot(complex(0,0))
