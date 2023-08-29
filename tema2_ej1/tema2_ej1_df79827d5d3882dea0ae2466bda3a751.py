import math
def menu():
    """MENU"""
    print("""******
    Calcular area
    *****

    1) Triangulo

    2) Rectangulo

    3) Rombo

    4) Circulo

    5) Salir
    """)

def area_triangulo(base,altura):
    resultado = int(base) * int(altura) /2
    print(resultado)
    return resultado

def area_rectangulo(base,altura):
    resultado = int(base) * int(altura)
    print(resultado)
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado = int(diagonal1) * int(diagonal2) / 2
    print(resultado)
    return resultado

def area_circulo(radio):
    resultado = int(radio) * int(radio) * math.pi
    print(resultado)
    return resultado

if __name__ == "__main__":
    pass
           