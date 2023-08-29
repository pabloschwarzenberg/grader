import math

def area_triangulo(base,altura):
    area_triangulo = (base * altura) / 2
    
    
    return area_triangulo
def area_rectangulo(base,altura):
    area_rectangulo = (base * altura)
    
    
    return area_rectangulo
def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1 * diagonal2) / 2
    
    
    return area_rombo
def area_circulo(radio):
    area_circulo = ((radio**2) * math.pi)
    
    
    return area_circulo
    
if __name__ == "__main__":
    print("Bienvenido a la calculadora de area")
    print(" 1.- Triangulo")
    print(" 2.- Rectangulo")
    print(" 3.- Rombo")
    print(" 4.- Circulo")
    ejercicio = int(input("Ingrese el numero correspondiente a la figura que quiere calcular su area: "))
    if ejercicio == 1:
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
        print(area_triangulo(base, altura))
        
    elif ejercicio == 2:
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
        print(area_rectangulo(base, altura))
        
    elif ejercicio == 3: 
        diagonal1 = int(input("Ingrese el valor de la primera diagonal: "))
        diagonal2= int(input("Ingrese el valor de la segunda diagonal: "))
        print(area_rombo(diagonal1, diagonal2))
        
    elif ejercicio == 4:
        radio = int(input("Ingrese el valor del radio: "))
        print(area_circulo(radio))
    else:
        print("ERROR: Por favor, ingrese un valor valido")