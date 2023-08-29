def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=3.141592653589793*radio*radio
    return area

if __name__ == "__main__":
    opcion=int(input("Ingrese una opcion\n(1)Triangulo\n(2)Rectangulo\n(3)Rombo\n(4)Circulo\n==> "))
    if opcion==1:
        base=eval(input("Ingrese la base"))
        altura=eval(input("Ingrese la altura"))
        area=area_triangulo(base,altura)
        print("El area es ", area)
    if opcion==2:
        
        base=eval(input("Ingrese la base"))
        altura=eval(input("Ingrese la altura"))
        area=area_rectangulo(base,altura)
        print("El area es ", area)
    if opcion==3:
        diagonal1=eval(input("Ingrese la diagonal 1: "))
        diagonal2=eval(input("Ingrese la diagonal 2: "))
        area=area_rombo(diagonal1,diagonal2)
        print("El area es ", area)
    if opcion==4:
        radio=eval(input("Ingrese el radio: "))
        area=area_circulo(radio)
        print("El area es ",area)
