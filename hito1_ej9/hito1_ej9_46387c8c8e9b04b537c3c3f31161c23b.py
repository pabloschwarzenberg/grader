#Sistema de Ecuaciones
def solucion_sistema_ecu(a,b,c,d,e,f):
    dete = a*e - b*d
    if dete != 0:
        x = (c * e - b * f)/dete
        y = (a * f - c * d)/dete
        print("x= ",x)
        print("y= ",y)
    else:
        print("No es posible realizar el sistema")


a = float(input("Ingrese los valores para a: "))
b = float(input("Ingrese los valores para b: "))
c = float(input("Ingrese los valores para c: "))
d = float(input("Ingrese los valores para d: "))
e = float(input("Ingrese los valores para e: "))
f = float(input("Ingrese los valores para f: "))

print(solucion_sistema_ecu(a,b,c,d,e,f))
