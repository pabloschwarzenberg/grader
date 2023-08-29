#Para resolver sistema de ecuaciones
def sistema(a1,b1,c1,a2,b2,c2):
    z = a1*b2 - b1* a2
    x=(c1*b2 - b1*c2)/z
    y=(a1*c2 - c1*a2)/z
    print("x=",x)
    print("y=",y)

print("Ingrese los valores de la primera ecuacion")
a1=int(input("Factor de x: "))
b1=int(input("Factor de y: "))
c1=int(input("Solucion de primera ecuacion: "))
a2=int(input("Factor de x: "))
b2=int(input("Factor de y: "))
c2=int(input("Solucion de segunda ecuacion: "))

print(sistema(a1,b1,c1,a2,b2,c2))
