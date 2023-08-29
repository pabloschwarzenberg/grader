def DeterminanteX(c,e,f,b):
    determinanteX = (c*e - f*b)
    return determinanteX

def DeterminanteY(a,f,d,c):
    determinanteY = (a*f - d*c)
    return determinanteY

def DeterminanteS(a,e,d,b):
    determinanteS = (a*e - d*b)
    return determinanteS

def SolucionX(determinantex,determinantes):
    return (determinantex / determinantes)

def SolucionY(determinantey,determinantes):
    return (determinantey/determinantes)

a = int(input("Ingrese el numero que acompaña al x en la 1 ecuacion: "))
b = int(input("Ingrese el numero que acompaña al y en la 1 ecuacion: "))
c = int(input("Ingrese el numero independiente en la 1 ecuacion: "))

d = int(input("Ingrese el numero que acompaña al x en la 2 ecuacion: "))
e = int(input("Ingrese el numero que acompaña al y en la 2 ecuacion: "))
f = int(input("Ingrese el numero independiente en la 2 ecuacion: "))

determinantex = DeterminanteX(c,e,f,b)
determinantey = DeterminanteY(a,f,d,c)
determinantes = DeterminanteS(a,e,d,b)

x , y = SolucionX(determinantex,determinantes) , SolucionY(determinantey,determinantes)
print("Resultados")
print("x=",x)
print("y=",y)