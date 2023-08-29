import math
def area_circulo(r):
     A=(math.pi)*(r**2)
     return A
def area_rectangulo(a,b):
     A=a*b
     return A
def area_triangulo(b,h):
     A=(b*h)/2
     return A
def area_rombo(d1,d2):
     A=(d1*d2)/(2)
     return A
     
  

if __name__ == "__main__":
    print("Hola.")
    print("Elige una figura para calcular su area: ")
    print("[1] CIRCULO")
    print("[2] RECTANGULO")
    print("[3] TRIANGULO")
    print("[4] ROMBO")
    
    f=int(input("Ingrese su opcion: "))  
    if f==1:
       A=area_circulo()
    elif f==2:
       A=area_rectangulo()
    elif f==3:
       A=area_triangulo()
    elif f==4:
       A=area_rombo()
    print("El area es: ",A)
    pass
           