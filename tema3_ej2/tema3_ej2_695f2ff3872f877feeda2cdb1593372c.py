import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        norma = math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
        return norma

    def __add__(self,v):
        sumax = self.x + v.x
        sumay = self.y + v.y
        sumaz = self.z + v.z
        vectorsuma = (sumax, sumay, sumaz)
        return vectorsuma


def suma_vectores(a,b):
    a = Vector
    b = Vector
    c = Vector.__add__(a,b)
    return c
