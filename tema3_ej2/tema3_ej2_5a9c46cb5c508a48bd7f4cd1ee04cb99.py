# crea la clase Vector y completa el código de la función suma_vectores usándola
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z  
        self.modulo = (x**2 + y**2 + z**2)**(1/2)
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return vector(x,y,z)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
    def norma(self):
        return self.modulo
    def suma_vectores(v1,v2):
        return v1+v2
    
    
           