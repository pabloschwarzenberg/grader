from math import pi
def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area
    

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=pi*(radio)**2
    return area

if __name__ == "__main__":
    if __name__=="triangulo":
        base=input(int("base:"))
        altura=input(int("altura:"))
        area_triangulo(base,altura)
    if __name__=="rectangulo":
        base=input(int("base:"))
        altura=input(int("altura:"))
        area_rectangulo(base,altura)
    if __name__=="rombo":
        diagonal1=input(int("diagonal1:"))
        diagonal2=input(int("diagonal2:"))
        area_rombo(diagonal1,diagonal2)    
    if __name__=="circulo":
        radio=input(int("radio:"))
        area_circulo(radio)