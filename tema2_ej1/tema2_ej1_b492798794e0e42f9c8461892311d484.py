def area_triangulo(base,altura):
    base*altura/2
    pass

def area_rectangulo(base,altura):
    base*altura
    pass

def area_rombo(diagonal1,diagonal2):
    diagonal1*diagonal2/2
    pass

def area_circulo(radio):
    2.14*radio**2
    pass

if __name__ == "__main__":
    base=int(input("Ingrese a: "))
    altura=int(input("Ingrese a: "))
    diagonal1=int(input("Ingrese a: "))
    diagonal2=int(input("Ingrese a: "))
    radio=int(input("Ingrese a: "))
    print("Menú")
    print("1.-Area triangulo")
    print("2.-Area rectangulo")
    print("3.-Area rombo")
    print("4.-Area circulo")
    x=int(input("ingrese que operacion desea realizar"))
    if x == 1:
        print(area_triangulo(base,altura))
    elif x == 2:
        print(area_rectangulo(base,altura))
    
    elif x == 3:
        print(area_rombo(diagonal1,diagonal2))
    
    elif x == 4:
        print(area_circulo(radio))
    pass
           