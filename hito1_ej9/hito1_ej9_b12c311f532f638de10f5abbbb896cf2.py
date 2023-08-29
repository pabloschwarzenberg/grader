#Sistema de Ecuaciones
a=int(input("escriba el primer numero: "))
b=int(input("escriba el segundo numero: "))
c=int(input("escriba el tercer numero: "))
d=int(input("escriba el cuarto numero: "))
e=int(input("escriba el quinto numero: "))
f=int(input("escriba el sexto numero: "))

#Ax+By=C
#Dx+Ey=F

def solucion(a,b,c,d,e,f):
    deter=a*e-b*d
    if deter!=0:
        x=(c*e - b*f)/deter
        y=(a*f - c*d)/deter
        return x,y
    else:
        return None,None
print(solucion(a,b,c,d,e,f))