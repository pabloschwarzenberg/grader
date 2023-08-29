from math import sqrt

class Vector3d:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        return sqrt( pow(self.x,2)+pow(self.y,2)+pow(self.z,2) )

    def suma_de_vectores(self,other):
        new_x=self.x + other.x
        new_y=self.y + other.y
        new_z=self.z + other.z
        vector_resultado = Vector3d(new_x,new_y,new_z)
        return vector_resultado

    def __add__(self, other):
        return self.suma_de_vectores(other)


if __name__ == "__main__":
    vector1 = Vector3d(1,4,6)
    vector2 = Vector3d(5,2,7)
    print((vector1+vector2).x == 6)

           