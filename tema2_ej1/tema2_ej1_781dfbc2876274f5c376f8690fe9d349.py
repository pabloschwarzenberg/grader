import math
def area_triangulo(base,altura):
    atri=(int(base)*int(altura))/2
    return atri

def area_rectangulo(base,altura):
    arec=(int(base)*int(altura))
    return arec

def area_rombo(diagonal1,diagonal2):
    arom=(int(diagonal1)*int(diagonal2))/2
    return arom

def area_circulo(radio):
    acir=((math.pi)*(int(radio)**2))
    return acir

if __name__ == "__main__":
    print("""----------------------------------------
Calculadora Geometrica
----------------------------------------
1. Area triangulo
2. Area rectangulo
3. Area rombo
4. Area circulo
5. Salir
----------------------------------------""")
    seleccion=0
    while seleccion!=5:
        seleccion=int(input("Selecciona una operacion:"))
        if seleccion==1:
            base=int(input("Ingrese Base: "))
            altura=int(input("Ingrese Altura: "))
            print("El area del triangulo es:", (area_triaangulo(base,altura)))
        elif seleccion==2:
            base=int(input("Ingrese Base: "))
            altura=int(input("Ingrese Altura: "))
            print("El area del rectangulo es:", (area_rectangulo(base,altura)))
        elif seleccion==3:
            diagonal1=int(input("Ingrese Diagonal1: "))
            diagonal2=int(input("Ingrese Diagonal2: "))
            print("El area del rombo es:", (area_rombo(diagonal1,diagonal2)))
        elif seleccion==4:
            radio=int(input("Ingrese Radio: "))
            print("El area del circulo es:", (area_circulo(radio)))

        elif seleccion==5:
            print("GoodBye")
            break
           