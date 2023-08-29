def area_triangulo(base,altura):
    area = (base * altura)/2
    return area
    

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area

def area_circulo(radio):
    import math
    area = math.pi * (radio)**2
    return area
    

if __name__ == "__main__":
    print("Elija una figura")
    print("1.- Rectángulo")
    print("2.- Triángulo")
    print("3.- Rombo")
    print("4.- Círculo")
    pick = int(input())
    if pick == 1:
      base = float(input("Defina una base: "))
      altura = float(input("Defina una altura: "))
      area_rectangulo(base, altura)
    if pick == 2:
      base = float(input("Defina una base: "))
      altura = float(input("Defina una altura: "))
      area_triangulo(base, altura)
    if pick == 3:
      diagonal1 = float(input("Defina la primera diagonal: "))
      diagonal2 = float(input("Defina la segunda diagonal: "))
      area_rombo(diagonal1,diagonal2)
    if pick == 4:
      radio = float(input("Defina un radio: "))
      area_circulo(radio)

           