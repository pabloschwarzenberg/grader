import math



def area_triangulo(base,altura):
    area=base*altura/2
    return area
    
def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2*(1/2)
    return area

def area_circulo(radio):
    area=(math.pi)*(radio**2)
    return area


print("1=Area triangulo")
print("2=Area rectangulo")
print("3=Area rombo")
print("4=Area circulo")

if __name__ == "__main__":
  opcion = int(input("ingresa opcion: "))
  if 1 <= opcion <=3 :
    a=int(input("Ingresa 1: "))
    b=int(input("Ingresa 2: "))
    if opcion==1:
        c=area_triangulo(a,b)
        print("El area es: ",c)
    elif opcion==2:
        c=area_rectangulo(a,b)
        print("El area es: ",c)
    elif opcion==3:
        c=area_rombo(a,b)
        print("El area es: ",c)
  elif opcion==4:
    a=int(input("Ingrese radio: "))
    b=area_circulo(a)
    print("El area es: ",b)
           