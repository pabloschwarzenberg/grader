import math
class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
           