import math
pi= math.pi


def area_triangulo(base,altura):
    area= (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area 

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2 
    return area
def area_circulo(radio):
    area= pi*(radio**2)
    return area 


print("**menu de opciones**")

print("1. Area triangulo")
print("2. Area rectangulo")
print("3. Area rombo")
print("4. Area circulo ")
