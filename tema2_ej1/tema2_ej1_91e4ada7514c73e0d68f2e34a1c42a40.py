def area_triangulo(base,altura):
    area=(base*altura)/2
    print(area)
    return(area)
def area_rectangulo(base,altura):
    area=(base*altura)
    print(area)
    return(area)
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    print(area)
    return(area)
def area_circulo(radio):
    import math
    area=radio**2*math.pi
    print(area)
    return(area)

if __name__ == "__main__":
    figura=input("ingrese la figura cuya área desea calcular: ")
    if figura == "triangulo":
        base=int(input("Ingrese el valor de la base: "))
        altura=int(input("Ingrese el valor de la altura: "))
        area_triangulo(base, altura)

    if figura == "rectangulo":
        base=int(input("Ingrese el valor de la base: "))
        altura=int(input("Ingrese el valor de la altura: "))
        area_rectangulo(base, altura)
          
    if figura == "rombo":
        diag1=int(input("Ingrese el valor de la diagonal 1: "))
        diag2=int(input("Ingrese el valor de la diagonal 2: "))
        area_rombo(diag1, diag2)
           
    if figura == "circulo":
        radio=int(input("Ingrese el valor del radio: "))
        area_circulo(radio)
