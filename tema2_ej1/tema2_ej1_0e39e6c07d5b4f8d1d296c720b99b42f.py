import math
def area_triangulo(base,altura):
        return (base*altura/2)

def area_rectangulo(base,altura):
        return (base*altura)

def area_rombo(diagonal1,diagonal2):
        return (diagonal1*diagonal2)/2

def area_circulo(radio):
       return math.pi*(radio**2)
         
if __name__ == "__main__":
    base=""
    altura=""
    diagonal1=""
    diagonal2=""
    radio=""
    print("0:area triangulo")
    print("1:area rectangulo")
    print("2:area rombo")
    print("3:area circulo")
    opcion = int(input())
    if opcion==0:
        base=int(input(": "))
        altura=int(input(": "))
    if opcion==1:
        base=int(input(": "))
        altura=int(input(": "))
    if opcion==2:
        diagonal1=int(input(": "))
        diagonal2=int(input(": "))
    if opcion==3:
        radio=int(input(": "))
   

