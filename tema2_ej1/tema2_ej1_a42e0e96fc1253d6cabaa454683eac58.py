import math
def area_triangulo(base,altura):
    a=(base*altura)/2
    return a

def area_rectangulo(base,altura):
    b=base*altura
    return b

def area_rombo(diagonal1,diagonal2):
    c=(diagonal1*diagonal2)/2
    return c

def area_circulo(radio):
    d=(math.pi)*radio*radio
    return d

    

           
if __name__ == "__main__":
    opcion=int(input("""Opciones de figuras para calcular areas
(1)Area triangulo
(2)Area rectangulo
(3)Area rombo
(4)Area circulo
El area de que figura desea calcular?:"""))
    if opcion==1 or opcion==2:
        base=int(input("ingrese la base de la figura:"))
        altura=int(input("ingrese la altura de la figura:"))
    if opcion==1:
        print(area_triangulo(base,altura))
    elif opcion==2:
        print(area_rectangulo(base,altura))
   
    elif opcion==3:
        diagonal1=int(input("ingrese la base de la figura:"))
        diagonal2=int(input("ingrese la altura de la figura:"))
        print(area_rombo(diagonal1,diagonal2))
                  
    elif opcion==4:
        radio=int(input("Ingrese el radio de la figura:"))
        print(area_circulo(radio))
    
