import math
def area_triangulo(base,altura):
    a1=base*altura*0.5
    return a1

def area_rectangulo(base,altura):
    a2=base*altura
    return a2

def area_rombo(diagonal1,diagonal2):
    a3=diagonal1*diagonal2*0.5
    return a3

def area_circulo(radio):
    a4=math.pi*radio**2
    return a4

if __name__ == "__main__":
    print("CALCULAR EL AREA DE: ")
    print("1) triangulo")
    print("2) rectangulo")
    print("3) rombo")
    print("4) circulo")
    opcion=int(input("ingrese su opcion : "))
    if opcion==1:
      base=float(input("base? : "))
      altura=float(input("altura? : "))
      print(area_triangulo(base,altura))
    elif opcion==2:
      base=float(input("base? : "))
      altura=float(input("altura : "))
      print(area_rectangulo(base,altura))
    elif opcion==3:
      d1=float(input("diagonal 1? : "))
      d2=float(input("diagonal 2? : "))
      print(area_rombo(d1,d2))
    elif opcion==4:
      radio=float(input("radio? : "))
      print(area_circulo(radio))
    
      
           