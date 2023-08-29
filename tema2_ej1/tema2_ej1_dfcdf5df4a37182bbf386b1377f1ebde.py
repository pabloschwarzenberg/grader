import math

def area_triangulo(base,altura):
    area_tri=(base*altura)/2
    return area_tri

def area_rectangulo(base,altura):
    area_rect=base*altura
    return area_rect

def area_rombo(diagonal1,diagonal2):
    area_romb=(diagonal1*diagonal2)/2
    return area_romb

def area_circulo(radio):
    area_circ=(radio**2)*math.pi
    return area_circ

if __name__ == "__main__":
    print("Bienvenido, ¿de qué desea calcular el área?")
    print("Puede escoger entre: Rectangulo, Rombo, Circulo")
    figura=input("Ingrese la figura escogida: ")
    if figura=="Rectangulo":
      print(area_rectangulo)
    elif figura=="Rombo":
      print(area_rombo)
    elif figura=="Circulo":
      print(area_circulo)
    else:
      print("Ingrese una figura valida")
      input("Reingrese una figura: ")
           