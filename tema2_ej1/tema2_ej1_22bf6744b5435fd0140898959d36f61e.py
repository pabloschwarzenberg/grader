def area_triangulo(base,altura):

    x=((int(base))*(int(altura)))/2
    
    return(x)

def area_rectangulo(base,altura):

    x=(int(base))*(int(altura))

    return(x)

def area_rombo(diagonal1,diagonal2):

    x=((int(diagonal1))*(int(diagonal2)))/2
    
    return(x)

def area_circulo(radio):

    import math

    x=(math.pi)*((radio)**2)

    return(x)

if __name__ == "__main__":

    print("1: Area del Triangulo")
    print("1: Area del Rectangulo")
    print("1: Area del Rombo")
    print("1: Area del Circulo")

    z=int(input("El area de que figura deseas calcular?: "))

    if z==1:
        area_triangulo(base,altura)

    elif z==2:
        area_rectangulo(base,altura)

    elif z==3:
        area_rombo(diagonal1,diagonal2)

    elif z==4:
        area_circulo(radio)
           