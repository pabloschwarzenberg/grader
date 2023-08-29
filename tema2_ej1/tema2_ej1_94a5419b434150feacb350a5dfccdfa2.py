import math
if __name__=="__main__":
    
    while True:
        
        print("1. Area de un triangulo")
        print("2. Area de un rectangulo")
        print("3. Area de un rombo")
        print("4. Area de un circulo")

        choose= int(input("Eliga la operación matemática que quiere hacer: "))
        while (choose>=1 and choose<=4):
        
            if (choose==1):
        
                base= int(input("Ingrese la base del triangulo: "))
                altura= int(input("Ingrese la base del triangulo: "))
                salida= area_triangulo(base,altura)
                print(salida)
            elif (choose==2):
                base= int(input("Ingrese la base del rectangulo: "))
                altura=  int(input("Ingrese la altura del rectangulo: "))
                salida=area_rectangulo(base,altura)
                print(salida)
            elif (choose==3):
                diagonal1= int(input("Ingrese la diagonal mayor del rombo: "))
                diagonal2= int(input("Ingrese la diagonal menor del rombo: "))
                salida= area_rombo(diagonal1,diagonal2)
                print(salida)
            else:
                radio= int(input("Ingrese el radio del circulo: "))
                salida=area_circulo(radio)
                print(salida)

def area_triangulo(base,altura):
    #base= int(input("Ingrese la base del triangulo: "))
    #altura= int(input("Ingrese la base del triangulo: "))
    return(base*altura)/2
    pass

def area_rectangulo(base,altura):

    #base= int(input("Ingrese la base del rectangulo: "))
    #altura=  int(input("Ingrese la altura del rectangulo: "))
    return base*altura
    print(Arec)

    pass

def area_rombo(diagonal1,diagonal2):
    #diagonal1= int(input("Ingrese la diagonal mayor del rombo: "))
    #diagonal2= int(input("Ingrese la diagonal menor del rombo: "))
    ##diagonal mayor por diagonal menor div 2##
    return (diagonal1*diagonal2)/2
    pass

def area_circulo(radio):
    #radio= int(input("Ingrese el radio del circulo: "))
    return math.pi*(radio**2)
    pass

