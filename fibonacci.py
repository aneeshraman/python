import sys
import math

def fibonacci():
    a = sys.maxsize
    b = sys.maxsize
    while True:
        c = a + b
        a = b
        b = c
        print(a)


fibonacci()
