import math
def area_triangulo(base,altura):
       if(n==1):
         base=int(input("ingrese la base:"))
         altura=int(input("ingrese la altura:"))
         area=(base*altura)/2
def area_rectangulo(base2,altura2):
       if(n==2):
         base2=int(input("ingrese la base:"))
         altura2=int(input("ingrese la altura:"))
         area2=base2*altura2
def area_rombo(diagonal1,diagonal2):
       if(n==3): 
         diagonal1=int(input("ingrese la diagonal1:"))
         diagonal2=int(input("ingrese la diagonal2:"))
         area3=(diagonal1*diagonal2)/2
def area_circulo(radio):
     if(n==4): 
         radio=int(input("ingrese el radio:"))
         area4=(radio*radio)*math.pi
         area4=radio*math.pi
if __name__ == "__main__":
    n=int(input("eliga la figura que desea calcular:"))
    print("El area de un triangulo de base",base,"y altura",altura,"debiera ser",area)
    print("El area de un rectangulo de lados",base2,"y",altura2,"debiera ser",area2)
    print("El area de un rombo con diagonales",diagonal1,"y",diagonal2,"debiera ser",area3)
    print("El area de un circulo de radio",radio,"debiera ser", area4)
                 
         
         
