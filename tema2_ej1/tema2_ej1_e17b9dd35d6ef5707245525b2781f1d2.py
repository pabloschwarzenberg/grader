from math import pi
def area_triangulo(base,altura):
    q = (base*altura)/2
    return(q)
    
def area_rectangulo(base,altura):
    p = base * altura
    return(p)
    
def area_rombo(diagonal1,diagonal2):
    x = (diagonal1 * diagonal2)/2
    return(x)

def area_circulo(radio):
    c = pi * (radio*radio)
    return(c)

if __name__ == "__main__":
 print("Figuras geometricas")
 print("1.-Triangulo")  
 print("2.-Rectangulo") 
 print("3.-Rombo") 
 print("4.-Circulo")
 a = int(input("Elige una figura para calcular su area:"))
 if a == 1:
   base = int(input("Ingresa la base:"))
   altura = int(input("Ingresa la altura:"))
   area_triangulo(base,altura)
 if a == 2:
   base = int(input("Ingresa la base:"))
   altura = int(input("Ingresa la altura:"))
   area_rectangulo(base,altura)
 if a == 3:
   diagonal1 = int(input("Ingresa la diagonal mayor:"))
   diagonal2 = int(input("Ingresa la diagonal menor:"))
   area_rombo(diagonal1,diagonal2)
 if a == 4:
   radio = int(input("Ingresa el radio:"))
   area_circulo(radio)

