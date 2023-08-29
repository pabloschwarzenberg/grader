def area_triangulo(base,altura):
    return (base*altura/2)
def area_rectangulo(base,altura):
    return (base*altura)

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2/2)
def area_circulo(radio):
    import math
    return (math.pi*radio*radio)

if __name__ == "__main__":
    figura=input("figura: ")
    if figura=="triangulo":
      base==int(input("base: "))
      altura==int(input("altura: "))
      print(str(area_triangulo(base,altura)))
    if figura==rectangulo:
      base==int(input("base: "))
      altura==int(input("altura: "))
      print(str(area_rectangulo(base,altura)))
    if figura=="rombo":
      diagonal1==int(input("diagonal1: "))
      diagonal2==int(input("diagonal2: "))
      print(str(area_rombo(diagonal1,diagonal2)))
    if figura=="circulo":
      radio==int(input("radio: "))
      print(str(area_circulo(radio)))