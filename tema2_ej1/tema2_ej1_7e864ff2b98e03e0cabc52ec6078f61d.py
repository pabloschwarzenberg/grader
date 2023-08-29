def area_triangulo(base,altura):
    area = base * altura / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area

def area_circulo(radio):
    area = 3.141592653589793 * (radio**2) 
    return area
figura = str()

if figura == "triangulo":

    base = float(input("Ingrese medida de la base: "))
    altura = float(input("Ingrese medida de la altura: "))
    

elif figura == "rectangulo":

    base = float(input("Ingrese medida de la base: "))
    altura = float(input("Ingrese medida de la altura: "))
   
elif figura == "rombo":

    diagonal1 = float(input("Ingrese medida de la diagonal 1: "))
    diagonal2 = float(input("Ingrese medida de la diagonal 2: "))
    
elif figura == "circulo":

    radio = float(input("Ingrese medida del radio: "))
   
  