import math as m
def area_triangulo(base,altura):
    area=(float(base)*float(altura))/2
    return area
    pass

def area_rectangulo(base,altura):
    area = (float(base) * float(altura))
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = (float(diagonal1)*float(diagonal2))/2
    return area
    pass

def area_circulo(radio):
    area = (float(radio)**2)* m.pi
    return area
    pass

tipo=""
a=0
b=0
A=0
k=""
if __name__ == "__main__":
    while k!="adios":
        tipo=input("ingrese tipo de figura\n->> ")
        if tipo=="triangulo":
            a=input("ingrese el numero de la base\n->> ")
            b=input("ingrese el numero de la altra\n->> ")
            A=area_triangulo(a,b)
            print("el area del %s es "%(tipo)+ str(A))
            k = "adios"

        elif tipo=="rectangulo":
            a=input("ingrese el numero de la base\n->> ")
            b=input("ingrese el numero de la altra\n->> ")
            A=area_rectangulo(a,b)
            print("el area del %s es "%(tipo)+ str(A))
            k = "adios"

        elif tipo=="rombo":
            a=input("ingrese el numero de la diagonal 1\n->> ")
            b=input("ingrese el numero de la diagonal 2\n->> ")
            A=area_rombo(a,b)
            print("el area del %s es "%(tipo)+ str(A))
            k = "adios"

        elif tipo == "circulo":
            a = input("ingrese el numero del radio\n->> ")
            A = area_circulo(a)
            print("el area del %s es "%(tipo)+ str(A))
            k = "adios"

        else:
            print("entrada incorrecta \nporfavor, ingrese solo:")
            print("- triangulo \n- rectangulo \n- rombo \n- circulo")

    pass       