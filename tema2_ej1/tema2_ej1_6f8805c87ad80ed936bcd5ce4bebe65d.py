import math
def area_triangulo(base,altura):
    area= (altura*base)/2
    print("El area es: ", area)
    return area

def area_rectangulo(base,altura):
    area=base*altura
    print("El area es: ", area)
    return area

def area_rombo(diagonal1,diagonal2):
    area= (diagonal1*diagonal2)/2
    print(area)
    return area

def area_circulo(radio):
    area= math.pi*(radio**2)
    print("El area es: ", area)
    return area
x=0
if __name__ == "__main__":
    x= int(input(""" 
1. Triangulo
2. Rectangulo
3. Rombo
4. Circulo
Seleccione el objeto del cual desea saber su area:"""))

if x==1:
    if __name__ == "__main__":
        base= float(input("Ingrese la base: "))
        altura= float(input("Ingrese la altura: "))
    area_triangulo(base,altura)
    
elif x==2:
    if __name__ == "__main__":
        base= float(input("Ingrese la base: "))
        altura= float(input("Ingrese la altura: "))
    area_rectangulo(base,altura)
        
elif x==3:
    if __name__ == "__main__":
        diagonal1= float(input("Ingrese diagonal1 : "))
        diagonal2= float(input("Ingrese diagonal2 : "))
    area_rombo(diagonal1,diagonal2)
        
elif x==4:
    if __name__ == "__main__":
        radio= float(input("Ingrese el radio de la circunferencia: "))
    area_circulo(radio)
