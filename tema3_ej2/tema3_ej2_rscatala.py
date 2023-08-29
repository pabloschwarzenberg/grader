# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        import math
        norma_sqr = self.x**2 + self.y**2 + self.z**2
        norma = math.sqrt(norma_sqr)
        return norma
    def __add__(self,other):
        v_x = self.x+other.x
        v_y = self.y+other.y
        v_z = self.z+other.z
        return Vector(v_x,v_y,v_z)
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)
        
def suma_vectores(v1,v2):
    v_x = v1.x + v2.x
    v_y = v1.y + v2.y
    v_z = v1.z + v2.z
    return Vector(v_x,v_y,v_z)
                            
if __name__ == "__main__":

    v1 = Vector(3,2,4)
    v2 = Vector(5,3,2)
    v3 = suma_vectores(v1,v2)
    print(v3)
    

        
           