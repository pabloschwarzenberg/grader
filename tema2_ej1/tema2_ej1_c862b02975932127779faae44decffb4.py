import math 
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area


if __name__ == "__main__":
    print ("Opciones:")    
    print ("(1) Triangulo")
    print ("(2) Rectangulo")
    print ("(3) Rombo")
    print ("(4) Circulo")    
    a=eval (input ("Qué area deseas calcular?"))
    if a==1:
        base=float(input("Ingresa base:"))
        altura=float(input("Ingresa altura:"))
        print (area_triangulo(base,altura))
    elif a==2:
        base=float(input("Ingresa base:"))
        altura=float(input("Ingresa altura:"))
        print (area_rectangulo(base,altura))
    elif a==3:
        diagonal1=float(input("Ingresa una diagonal:"))
        diagonal2=float(input("Ingresa la otra diagonal:"))
        print (area_rombo(diagonal1,diagonal2))
    elif a==4:
        radio=float(input("Ingresa radio:"))
        print (area_circulo(radio))
        