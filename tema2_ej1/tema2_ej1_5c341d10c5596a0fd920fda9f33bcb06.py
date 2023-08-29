import math
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
    area=(radio**2)*math.pi
    return area
if __name__ == "__main__":
    count=0
    while count<1:
        print("Bienvenido a la calculadora geométrica, ¿Qué desea calcular?")
        print("""1-Área Triángulo
2-Área Rectángulo
3-Área Rombo
4-Área Círculo""")
        n=int(input())
        if n==1:
            b=float(input("Ingrese la base de su triángulo"))
            h=float(input("Ingrese la altura de su triángulo"))
            area=area_triangulo(b,h)
            print("el área de su triángulo es:",area)
        elif n==2:
            b=float(input("Ingrese la base de su rectangulo"))
            h=float(input("Ingrese la altura de su rectangulo"))
            area=area_rectangulo(b,h)
            print("el área de su rectangulo es:",area)
        elif n==3:
            d1=float(input("Ingrese la diagonal 1 de su rombo"))
            d2=float(input("Ingrese la diagonal 2 de su rombo"))
            area=area_rombo(d1,d2)
            print("el área de su rombo es:",area)
        elif n==4:
            r=float(input("Ingrese el radio de su circulo"))
            area=area_circulo(r)
            print("el área de su circulo es:",area)
        f=input("¿Desea hacer otro cálculo?")
        f=f.upper()
        if f=="NO":
                count+=1                
            
           