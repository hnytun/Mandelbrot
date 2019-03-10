cimport numpy as np

def sum_np(np.ndarray[np.int64_t, ndim=1] A):
    cdef unsigned long s = 0
    for a in A:
        s += a
    return s

def calculateMandelBrot(np.complex128_t a):

    z=complex(10,10)
