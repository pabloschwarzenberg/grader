# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        norma = ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5
        return norma

    def __add__(self,other):
        r = Vector(0, 0, 0)
        r.x = self.x + other.x
        r.y = self.y + other.y
        r.z = self.z + other.z
        return r

    def suma_vectores(self,v1,v2):
        x_ = v2.x + v1.x
        y_ = v2.y + v1.y
        z_ = v2.z + v1.z
        return x_,y_,z_
        
if __name__ == "__main__":
    v = Vector(int(input()),int(input()),int(input()))
    u = Vector(int(input()),int(input()),int(input()))

    print(v.suma_vectores(u,v))