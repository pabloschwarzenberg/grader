def area_triangulo(altura,base):
    area=0.5*altura*base
    return area
def area_rectangulo(altura,base):
    area=altura*base
    return area
def area_rombo(diagonal1,diagonal2):
    area=0.5*diagonal1*diagonal2
    return area
pi=3.1415926535897932
def area_circulo(radio):
    area=pi*radio*radio
    return area
print("(1)rectángulo")
print("(2)triángulo")
print("(3)rombo")
print("(4)círculo")
if __name__=="__main__":
    figura=int(input("Ingrese la figura a la que quiere calcular el área: "))
    if figura==1:
        altura=int(input("Ingrese altura: "))
        base=int(input("Ingrese la base: "))
        print("Área: ",area_rectangulo(altura,base))
    elif figura==2:
        altura=int(input("Ingrese altura: "))
        base=int(input("Ingrese la base: "))
        print("Área: ",area_triangulo(altura,base))
    elif figura==3:
        diagonal1=int(input("Ingrese diagonal 1: "))
        diagonal2=int(input("Ingrese diagonal 2: "))
        print("Área: ",area_rombo(diagonal1,diagonal2))
    else:
        radio=int(input("Ingrese radio: "))
        print("Área: ",area_circulo(radio))
