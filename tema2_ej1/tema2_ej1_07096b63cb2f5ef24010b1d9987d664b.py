import math

print("1) Area Triangulo  2) Area Rectangulo 3) Area Rombo   4) Area Circulo")

eligio = "1"

if eligio == "1":

    print("Area Triangulo")


    def area_triangulo(base, altura):
        pass
        resultado = base * altura / 2
        return resultado


    print(area_triangulo(11, 7))

elif eligio == "2":

    print("Area Rectangulo")

    def area_rectangulo(base, altura):
        pass
        resultado = base * altura
        return resultado

    print(area_rectangulo(10,6))


elif eligio == "3":
    print("Area Rombo")


    def area_rombo(diagonal1, diagonal2):
        pass
        resultado = diagonal1 * diagonal2
        return resultado


    print(area_rombo(5, 7))

elif eligio == "4":
    print("Area Circulo")


    def area_circulo(radio):
        pass
        resultado = math.pi * radio * radio
        return resultado


    print(area_circulo(7))


else:
    input("fin del programa")
