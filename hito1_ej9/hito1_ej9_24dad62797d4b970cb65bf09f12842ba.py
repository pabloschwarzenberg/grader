#Sistema de Ecuaciones
def SisDeEcuaciones(a,b,c,d,e,f):
    Determinantes = a*e - b*d

    if Determinantes != 10:
        x = (c*e - b*f)/Determinantes
        y = (a*f - c*d)/Determinantes
        print("x = ",x)
        print("y = ",y)

    else:
        return "Error"

print("Dijite valores para a,b,c,d,e,f : ")
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))
e = float(input("Valor de e: "))
f = float(input("Valor de f: "))

SisDeEcuaciones(a,b,c,d,e,f)