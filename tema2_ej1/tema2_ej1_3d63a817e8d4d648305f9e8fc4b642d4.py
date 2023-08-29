import math
def area_triangulo(base,altura):
    resultado=(base*altura)/2
    return resultado

def area_rectangulo(base,altura):
    resultado=(base*altura)
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado=(diagonal1*diagonal2)/2
    return resultado

def area_circulo(radio):
    resultado = (math.pi)*((radio)**2)
    return resultado

if __name__=="__main__":
    print("---Menú---")
    print("Calcular Área triangulo opción 1")
    print("Calcular Área rectangulo  opción 2")
    print("calcular Área rombo opción 3")
    print("Calcular Área circulo opción 4")
    print("----------")

    opcion = int(input("ingrese opción : "))

    if opcion == 1:
        base=int(input("ingrese base triángulo :"))
        altura=int(input("ingrese altura triángulo :"))
        resultado = area_triangulo(base,altura)
        
    elif opcion == 2:
        base=int(input("ingrese base rectángulo :"))
        altura=int(input("ingrese altura rectángulo :"))
        resultado = area_rectangulo(base,altura)
        
        
    elif opcion == 3:
        diagonal1=int(input("ingrese diagonal 1 :"))
        diagonal2=int(input("ingrese diagonal 2 :"))
        resultado = area_rombo(diagonal1,diagonal2)

    elif opcion == 4:
        radio=int(input("ingrese radio del círculo :"))
        resultado = area_circulo(radio)

    print(resultado)