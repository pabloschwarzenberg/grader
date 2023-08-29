import math

def area_triangulo(base,altura):
    area1 = base*altura/2    
    return area1

def area_rectangulo(base,altura):
    area2 = base*altura
    return area2

def area_rombo(diagonal1,diagonal2):
    area3 = diagonal1*diagonal2/2 
    return area3
    
def area_circulo(radio):
    area4 = math.pi*radio**2
    return area4

if __name__ == "__main__":
    menu = 1
    while menu == 1:
        opcion = int(input(" Ingrese una opcion: "))
        if opcion == 1:
            base = int(input("Ingrese base")) 
            altura = int(input("Ingrese altuira"))
            print(area_triangulo(base, altura))    
              
        elif opcion == 2:
            base = int(input("Ingrese base ")) 
            altura = int(input("Ingrese altura "))
            print(area_rectangulo(base, altura))
              
        elif opcion == 3:
            diagonal1 = int(input("Ingrese diagonal1 "))
            diagonal2 = int(input("Ingrese diagonal2"))
            print(area_triangulo(diagonal1, diagonal2))
               
        elif opcion == 4:
            radio = int(input("Ingrese Radio ")) 
            print(area_circulo(radio))
              
        elif opcion == 5:
            menu = 0