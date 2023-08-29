def area_triangulo(base,altura):
    return (base*altura)/2
    
    pass

def area_rectangulo(base,altura):
    return (base*altura)
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
    pass
import math
def area_circulo(radio):
    return (radio**2)*math.pi
    pass

if __name__ == "__main__":
    menu=input("Que es lo que desea calcular(area del triangulo, area del rectangulo,area del rombo,area del circulo): ")
    if menu =="area del triangulo":
        print(area_triangulo(base,altura))
    elif menu=="area del rectangulo":
        print(area_rectangulo(base,altura))
    elif menu =="area del rombo":
        print(area_rombo(diagonal1,diagonal2))
    elif menu =="area del circulo":
        print(area_circulo(radio))
        

           