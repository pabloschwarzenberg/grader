#Sistema de Ecuaciones
a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
c=int(input("ingrese un numero: "))
d=int(input("ingrese un numero: "))
e=int(input("ingrese un numero: "))
f=int(input("ingrese un numero: "))
def sistema(a,b,c,d,e,f):
    divisor=(a*e - b*d)
    x=(c*e - b*f)/divisor
    x=round(x,1)
    y=(a*f - d*c)/divisor
    y=round(y,1)

    return [x,y]

solucion=sistema(a,b,c,d,e,f)
print(solucion)