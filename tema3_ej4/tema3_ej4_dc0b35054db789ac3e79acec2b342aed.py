class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __repr__(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)

    def a_numero(self):
        return self.num/self.den

    # Definir el método __add__ para sobrecargar la operación +
    def __add__(self, other):
        # Sumar las fracciones usando el mínimo común múltiplo de los denominadores
        mcm = self.den * other.den # Usar el producto de los denominadores como mcm
        r = Fraccion(0, 0) # Crear una fracción vacía para guardar el resultado
        r.num = (mcm // self.den) * self.num + (mcm // other.den) * other.num # Sumar los numeradores multiplicados por el factor correspondiente
        r.den = mcm # Asignar el mcm al denominador del resultado
        return r # Retornar el resultado

    # Definir el método __sub__ para sobrecargar la operación -
    def __sub__(self, other):
        # Restar las fracciones usando el mínimo común múltiplo de los denominadores
        mcm = self.den * other.den # Usar el producto de los denominadores como mcm
        r = Fraccion(0, 0) # Crear una fracción vacía para guardar el resultado
        r.num = (mcm // self.den) * self.num - (mcm // other.den) * other.num # Restar los numeradores multiplicados por el factor correspondiente
        r.den = mcm # Asignar el mcm al denominador del resultado
        return r # Retornar el resultado

    # Definir el método __truediv__ para sobrecargar la operación /
    def __truediv__(self, other):
        # Dividir las fracciones usando la regla de invertir y multiplicar
        r = Fraccion(0, 0) # Crear una fracción vacía para guardar el resultado
        r.num = self.num * other.den # Multiplicar los numeradores por los denominadores cruzados
        r.den = self.den * other.num # Multiplicar los denominadores por los numeradores cruzados
        return r # Retornar el resultado

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)

         