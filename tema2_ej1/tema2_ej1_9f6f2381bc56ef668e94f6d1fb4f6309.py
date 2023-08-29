import math
def area_triangulo(base,altura):
    areat=(base*altura)/2
    return areat

def area_rectangulo(base,altura):
    arear=base*altura
    return arear

def area_rombo(diagonal1,diagonal2):
    abeam=(diagonal1*diagonal2)/2
    return abeam

def area_circulo(radio):
    pi1=math.pi
    areair=pi1*radio**2
    return areair

if __name__ == "__main__":
   print("1=triángulo , 2=rectángulo, 3=rombo, 4=círculo")
   resultado=int(input("Ingrese el número de la figura a la cuál quiere calcular su área: ",))

   if resultado==1:
     base0=int(input("Ingrese el valor de la base del triángulo: ",))
     altura0=int(input("Ingrese el valor de la altura del triángulo: ",))
     print("El área del triángulo es: ",area_triangulo(base0,altura0))
   elif resultado==2:
     base1=int(input("Ingrese el valor de la base del rectángulo: ", ))
     altura1=int(input("Ingrese el valor de la altura del rectángulo: ", ))
     print("El área del rectángulo es: ",area_rectangulo(base1,altura1))
   elif resultado==3:
     diagonal1=int(input("Ingrese el valor de la diagonal mayor del rombo: ", ))
     diagonal2=int(input("Ingrese el valor de la diagonal menor del rombo: ", ))
     print("El área del rombo es: ",area_rombo(diagonal1,diagonal2))
   elif resultado==4:
     radio=int(input("Ingrese el valor del radio del círculo: ", ))
     print("El área del círculo es: ", area_circulo(radio))
   else:
     print("Ingrese un número del menú:", )
           