import math
pi=math.pi
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=pi*radio*radio
    return area

print("Determinar àrea de")
print("1)Triangulo")
print("2)Rectàngulo")
print("3)Rombo")
print("4)Cìrculo")
if __name__=="__main__":
    aaa=int(input(":"))
    print("Determinar àrea de ",aaa)
    if aaa==1:
        base=eval(input("indica el valor de la base:"))
        altura=eval(input("Indica el valor de la altura:"))
        print(area_triangulo(base,altura))
    elif aaa==2:
        base=eval(input("indica el valor de la base:"))
        altura=eval(input("Indica el valor de la altura:"))
        print(area_rectangulo(base,altura)) 
    elif aaa==3:
        diagonal1=eval(input("indica el valor de la diagonal1:"))
        diagonal2=eval(input("Indica el valor de la diagonal2:"))
        print(area_rombo(diagonal1,diagonal2))
    elif aaa==4:
        radio=eval(input("indica el valor del radio:"))
        print(area_circulo(radio))
