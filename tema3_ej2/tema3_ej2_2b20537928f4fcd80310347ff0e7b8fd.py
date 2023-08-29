class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    @staticmethod
    def suma_vectores(v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return Vector(x, y, z)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("Operands must be instances of Vector")
