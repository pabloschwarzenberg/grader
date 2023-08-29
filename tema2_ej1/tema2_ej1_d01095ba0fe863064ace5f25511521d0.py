def area_triangulo(base,altura):
    area = float((base*altura)/2)
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = ((diagonal1*diagonal2)/2)
    return area

def area_circulo(radio):
    import math
    area = (math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    figura_a_calcular=input("A que figura calculara su area?",)
    if figura_a_calcular=="rectangulo":
       print (area_rectangulo(base,altura))
    if figura_a_calcular=="triangulo":
       print (area_triangulo(base,altura))
    if figura_a_calcular=="rombo":
       print (area_rombo(diagonal1,diagonal2))
    if figura_a_calcular=="circulo":
       print (area_circulo(radio))
           