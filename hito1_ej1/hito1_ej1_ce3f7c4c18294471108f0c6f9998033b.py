#Nota final
def prom(a,b,c,d):
    prom = 0.3*a + 0.3*b + 0.3*c + 0.1*d
    return prom

PT = float(input("ingrese pt: "))
PI = float(input("ingrese pi: "))
NE= float(input("ingrese ne: "))
PP = float(input("ingrese pp: "))

print("el promedio es", round(prom(PT, PI, NE, PP), 1))