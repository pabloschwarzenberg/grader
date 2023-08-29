class Vector:
    def __init__(self, x ,y ,z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        a=(self.x)**2
        b=(self.y)**2
        c=(self.z)**2
        return((a+b+c)**(1/2))

    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        c = self.z + other.z
        return Vector(a,b,c)
def suma_vectores(v1, v2):
        a1 = v1.x + v2.x
        b1 = v1.y + v2.y
        c1 = v1.z + v2.z
        return Vector(a1, b1, c1)

