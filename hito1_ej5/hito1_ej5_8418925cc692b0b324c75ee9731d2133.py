#Cálculo del dígito verificador de un rut
numero=int(input("Ingrese su RUT sin puntos hasta el guión:"))
a=numero//10000000
i=numero%10000000
b=i//1000000
j=i%1000000
c=j//100000
w=j%100000
d=w//10000
l=w%10000
e=l//1000
m=l%1000
f=m//100
n=m%100
g=n//10
h=n%10
x=2*h+3*g+4*f+5*e+6*d+7*c+2*b+3*a
y=x//11
z=x-(11*y)
Código_Verificador=11-z
if(9>=Código_Verificador>=0):
    print("dv=",Código_Verificador)
elif(Código_Verificador==11):
    print("dv=",0)
elif(Código_Verificador==10):
    print("dv=","k")
else:
    print("El RUT fue mal ingresado")
    