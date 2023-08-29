import math
def area_triangulo(base,altura):
    area = int (base) * int (altura) / 2.0

def area_rectangulo(base,altura):
    area = int(base) * int(altura)

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2

def area_circulo(radio):
    area = (math.pi*(radio**2))
    

if __name__ == "__main__":
    print(area_triangulo(int(input("ingrese base y altura: "))))
    print(area_rectangulo(int(input("ingrese base y altura: ")))))
    print(area_rombo(int(input("ingrese diafonal1 y diagonal2: ")))))
    print(area_circulo(int(input("ingrese radio:  ")))))
           