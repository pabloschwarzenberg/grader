from math import pi
def area_triangulo(base,altura):
    base1=float(base)
    altura1=float(altura)
    return((base1*altura1)/2)

def area_rectangulo(base,altura):
    base2=float(base)
    altura2=float(altura)
    return(base2*altura2)

def area_rombo(diagonal1,diagonal2):
    diagonal12=float(diagonal1)
    diagonal22=float(diagonal2)
    return(diagonal12*((diagonal22)/2))

def area_circulo(radio):
    radio_2=float(radio)
    return((radio_2**2)*pi)
print(area_circulo)
"if __name__ == "#__main__":"

"""
def area(opcion,dimension1,dimension2):
    if opcion=="1":
        print(area_triangulo(dimension1,dimension2))
    if opcion=="2":
        print(area_rectangulo(dimension1,dimension2))
    if opcion=="3":
        print(area_rombo(dimension1,dimension1))
    if opcion=="4":
        #radio=input("Radio: ")
        print(area_circulo(dimension1))

a=input()
b=input()
c=input()
area(a,b,c)
"""
