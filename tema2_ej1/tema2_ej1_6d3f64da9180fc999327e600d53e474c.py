import math
class cuadrado:
    def _init_(self):
        self.lado1=int(input("Ingresa el lado del cuadrado: "))
    def area(self):
        area1=self.lado1*self.lado1
        print("El area es: ",area1)
    def perimetro(self):
        perimetro1=self.lado1*4
        print("El perimetro es: ",perimetro1)
class rectangulo:
    def _init_(self):
        self.lado1=int(input("Ingrese el valor del primer lado: "))
        self.lado2=int(input("Ingrese el valor del segundo lado: "))
    def area(self):
        area1=self.lado1*self.lado2
        print("El area es: ",area1)
    def perimetro(self):
        perimetro1=(self.lado1*2)+(self.lado2*2)
        print("El perimetro es: ",perimetro1)
class circulo:
    def _init_(self):
        self.lado1=int(input("Ingrese el valor del radio:  "))
    def area(self):
        area1=self.lado1**2*math.pi
        print("El area es: ",area1)
    def perimetro(self):
        perimetro1=2*math.pi*self.lado1
        print("El perimetro es: ",perimetro1)
contador=0
while contador==0:
    opcion=int(input("Elija su opcion: 1.-Cuadrado 2.-Rectangulo 3.-Circulo 4.-Salir  "))
    if opcion==1:
        c=cuadrado()
        c.area()
        c.perimetro()
    elif opcion==2:
        r=rectangulo()
        r.area()
        r.perimetro()
    elif opcion==3:
        c=circulo()
        c.area()
        c.perimetro()
    elif opcion==4:
        contador+=1
print("Se ha finalizado el programa")           