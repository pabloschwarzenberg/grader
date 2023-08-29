def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area
def area_circulo(radio):
    import math
    area=math.pi*(radio**2)
    return area
if __name__ == "__main__":
    figura=int(input("Que area deseas consultar, (1)triangulo (2)rectangulo (3)rombo (4)circulo: "))
    if figura==1:
      base=eval(input("Ingresa base triangulo: "))
      altura=eval(input("Ingresa altura triangulo: "))
      print(area_triangulo(base,altura))
    elif figura==2:
      base=eval(input("Ingresa base rectangulo: "))
      altura=eval(input("Ingresa altura rectangulo: "))
      print(area_rectangulo(base,altura))
    elif figura==3:
      diagonal1=eval(input("Ingresa la diagonal mayor: "))
      diagonal2=eval(input("Ingresa la diagonal menor: "))
      print(area_rombo(diagonal1,diagonal2))
    elif figura==4:
      radio=eval(input("Ingresa el radio"))
      print(area_circulo(radio))