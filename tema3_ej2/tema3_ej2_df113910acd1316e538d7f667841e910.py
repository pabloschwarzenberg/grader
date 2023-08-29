# crea la clase Vector y completa el código de la función suma_vectores usándolaclass Vectores:
    def __init__(self,x,y,z):
        self.norma = pow(x**2 + y**2 + z**2)

    def suma_vectores(self,v1,v2):

        self.suma = v1 + v2

        return self.suma
           