# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt, asin
class Vector:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    def __add__(self,other):
        x=Vector(self.x + other.x, self.y+ other.y, self.z + other.z)
        return x
    def suma_vectores(self, other):
        return x
    def norma(self):
        return sqrt((self._x)*2 + (self._y)*2 + (self._z)*2)
