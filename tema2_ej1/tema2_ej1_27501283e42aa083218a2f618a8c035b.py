from math import pi
def area_triangulo(base,altura):
    resultado = (base * altura) / 2
    return(resultado)

def area_rectangulo(base,altura):
    resultado = (base * altura)
    return(resultado)
    

def area_rombo(diagonal1,diagonal2):
    resultado = (diagonal1 * diagonal2)/ 2
    return(resultado)

def area_circulo(radio):
    resultado = pi * (radio**2)
    return(resultado)

if __name__ == "__main__":
    area_deseada = input()
    if area_deseada == "triangulo":
        b = float(input())
        a = float(input())
        print("Su area es:", area_triangulo(b,a))

    if area_deseada == "rectangulo":
        b = float(input())
        a = float(input())
        print("Su area es:", area_rectangulo(b, a))

    if area_deseada == "rombo":
        d1 = float(input())
        d2 = float(input())
        print("Su area es:", area_rombo(d1, d2))

    if area_deseada == "circulo":
        ra = float(input())
        print("Su area es:", area_circulo(ra))
