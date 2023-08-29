import cmath

# Area de un triagulo = (base * altura) / 2
def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

# Area de un rectangulo = base * altura
def area_rectangulo(base,altura):
    area = base * altura
    return area

# Area de un rombo = (diagonal1 * diagonal2) / 2
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

# Area de un circulo = Pi * radio ** 2
def area_circulo(radio):
    area = cmath.pi * (radio ** 2)
    return area

if __name__ == "__main__":
    pass