def area_triangulo(base,altura):

    base=int(base)

    altura=int(altura)

    area=(base*altura)/2

    return area

def area_rectangulo(base,altura):

    base=int(base)

    altura=int(altura)
    
    area= base*altura

    return area

def area_rombo(diagonal1,diagonal2):

    diagonal1=int(diagonal1)

    diagonal2=int(diagonal2)

    area= (diagonal1*diagonal2)/2

    return area

    

def area_circulo(radio):

    import math

    radio=int(radio)

    area= math.pi*radio*radio

    return area


if __name__ == "__main__":

    print("(1)Triángulo.")

    print("(2)Reactángulo.")

    print("(3)Rombo.")

    print("(4)Círculo.")

    a=input("Seleccione el área a calcular:")

    a=int(a)

    if a==1:

        b=input("Inserte base:")

        c= input("Inserte altura:")

        d=area_triangulo(b,c)

        print(d)

    if a==2:

        b=input("Inserte base:")

        c= input("Inserte altura:")

        d=area_rectangulo(b,c)

        print(d)

    if a==3:

        b=input("Inserte diagonal 1:")

        c=input("Inserte diagonal 2:")

        d=area_rombo(b,c)

        print(d)

    if a==4:

        r=input("Inserte el radio:")

        d=area_circulo(r)

        print(d)

    pass
           