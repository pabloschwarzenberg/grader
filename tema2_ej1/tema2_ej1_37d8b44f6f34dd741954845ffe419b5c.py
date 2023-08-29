import math

def area_rectangulo(largo,ancho):
    areaRec = largo * ancho
    return areaRec

def area_triangulo(base,altura):
    areaTria = (base * altura)/2
    return areaTria

def area_rombo(diagonalMa,diagonalMe):
    areaRom = (diagonalMa * diagonalMe)/2
    return areaRom

def area_circulo(radio):
    areaCir = math.pi * radio**2
    return areaCir

if __name__ == "__main__":
    figura = input("Ingrese la figura que quiera calcular su area ->")
    
    if figura == "Rectangulo" or figura == "rectangulo":
        num1 = int(input("Ingrese el largo del rectangulo ->"))
        num2 = int(input("Ingrese el ancho del rectangulo ->"))
        area_rectangulo(num1,num2)
        print(int(area_rectangulo(num1,num2)))
        
        
    if figura == "Triangulo" or figura == "triangulo":
        num1 = int(input("Ingrese la base del triangulo ->"))
        num2 = int(input("Ingrese la altura del triangulo ->"))
        
        area_triangulo(num1,num2)
        print(int(area_triangulo(num1,num2)))
        
    if figura == "Rombo" or figura == "rombo":
        num1 = int(input("Ingrese la madida de la Diagonal mayor ->"))
        num2 = int(input("Ingrese la medida de la Diagonal menor ->"))
        
        area_rombo(num1,num2)
        print(int(area_rombo(num1,num2)))
        
    if figura == "Circulo" or figura == "circulo":
        num1 = int(input("Ingrese el radio del circulo ->"))
        
        area_circulo(num1)
        print(int(area_circulo(num1)))