# Calculadora Geométrica
from math import pi

def area_triangulo(b, h):
    A = (b * h) / 2
    
    return A

def area_rectangulo(b, h):
    A = b * h
    
    return A

def area_rombo(d_1, d_2):
    A = (d_1 * d_2) / 2
    
    return A

def area_circulo(r):
    A = pi * (r ** 2)
    
    return A

if __name__ == "__main__":
    while True:
        print("Calculadora Geométrica\n- - - - - - - - - - - - - -\n    1.- Área de rectángulo\n    2.- Área de triángulo\n    3.- Área de rombo\n    4.- Área de círculo\n    5.- Salir\n")
        
        op_menu = input("Ingrese una opción: ")
        
        if op_menu == '1':
            base = int(input("\nIngrese la base del rectángulo: "))
            altura = int(input("Ingrese la altura del rectángulo: "))
            
            area = area_rectangulo(base, altura)
            
            print("\nEl área del rectángulo es:", area, "\n")
        elif op_menu == '2':
            base = int(input("\nIngrese la base del triángulo: "))
            altura = int(input("Ingrese la altura del triángulo: "))
            
            area = area_triangulo(base, altura)
            
            print("\nEl área del triángulo es:", area, "\n")
        elif op_menu == '3':
            diagonal_1 = int(input("\nIngrese la diagonal mayor del rombo: "))
            diagonal_2 = int(input("Ingrese la diagonal menor del rombo: "))
            
            area = area_rombo(diagonal_1, diagonal_2)
            
            print("\nEl área del rombo es:", area, "\n")
        elif op_menu == '4':
            radio = int(input("\nIngrese el radio del círculo: "))
            
            area = area_circulo(radio)
            
            print("\nEl área del círculo es:", area, "\n")
        elif op_menu == '5':
            break