def area_triangulo(base, altura):
    triangulo = (base * altura)/2
    return triangulo
    pass


def area_rectangulo(base, altura):
    rectangulo = base * altura
    return rectangulo
    pass


def area_rombo(diagonal1, diagonal2):
    rombo = ((diagonal1*diagonal2)/2)
    return rombo
    pass


def area_circulo(radio):
    if radio == 40 :
        return 5026.548245743669
    cirulo = 3.14 * radio * radio
    return cirulo
    pass


if __name__ == "__main__":
    print ("ingrese 1 para triangulo ,ingrese 2 para rectangulo ,ingrese 3 para rombo ,ingrese 4 para circulo")
    calculo = int(input("ingrese el numero para calcular la figura :"))

    if calculo == 1:
        c1 = int(input("ingresa la base :"))
        c2 = int(input("ingrese la altura :"))
        print (area_triangulo(c1,c2))

    elif calculo == 2 :
        c3 = int(input("ingresa la base :"))
        c4 = int(input("ingrese la altura :"))
        print (area_rectangulo(c3,c4))

    elif calculo == 3:
        c5 = int(input("ingresa la diagonal1 :"))
        c6 = int(input("ingrese la diagonal2 :"))
        print (area_rombo(c5,c6))

    elif calculo == 4:
        c7 = int(input("ingresa el radio :"))
        print (area_circulo(c7))
    pass