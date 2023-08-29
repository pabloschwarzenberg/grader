def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
 def area_triangulo(base,altura):
    base = float(input("ingresa la base: "))
    altura = float(input("ingresa la altura: "))
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
    base = float(input("ingresa la base: "))
    altura = float(input("ingresa la altura: "))
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    diagonal1 = float(input("ingresa la diagonal 1: "))
    diagonal2 = float(input("ingresa la diagonal 2: "))
    area = (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    radio = float(input("ingresa el radio del circulo: "))
    pi = 3,1416
    area =  pi*radio**2
    return area
    
   

menu()
    
          