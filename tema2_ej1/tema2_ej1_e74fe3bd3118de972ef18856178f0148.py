def suma_divisores(a):
    suma = 0
    for i in range (1, a):
     if a % i == 0:
       suma += i
    return suma, suma == 1
#areas de figuras
def area_triangulo(base, altura):
    return base * altura / 2
def area_rectangulo(base, altura):
    return base * altura
def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2
def area_circulo(radio):
    import math
    return math.pi * radio ** 2
if __name__ == "__main__":
    pass