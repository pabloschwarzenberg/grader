from math import pi

def menu ():
    
    if __name__ == "__main__":

        print("\nFIGURAS A CALCULAR")
        print("\nA. Triangulo")
        print("B. Rectangulo")
        print("C. Rombo")
        print("D. Circulo\n")
        print("AVISO!!! Ingrese unicamente la letra que corresponda a la figura a calcular.\n")

def area_triangulo(base, altura):   # Triangulo
   
    area = (base * altura) / 2
    return area

def area_rectangulo(base, altura):  # Rectangulo
    
    area = base * altura
    return area

def area_rombo(diagonal_mayor, diagonal_menor):  # Rombo
    
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

def area_circulo(radio):  # Circulo
    
    area = pi * radio** 2
    return area
 

if __name__ == "__main__":
    
    estado = True
    while estado == True:

        menu()
        opcion = input("Ingresa una opción: ")
        opcion = opcion.upper()
        print()

        if opcion == "A":
            print(area_triangulo(int(input("Base: ")), int(input("Altura: "))))
            estado = False
        
        if opcion == "B":
            print(area_rectangulo(int(input("Base: "), int(input("Altura: ")))))
            estado = False
        
        if opcion == "C":
            print(area_rombo(int(input("Diagonal Mayor: ")), int(input("Diagonal Menor: "))))
            estado = False
        
        if opcion == "D":
            print(area_circulo(int(input("Radio: "))))
            estado = False