#Cálculo del dígito verificador de un rut
x=int(input("Ingrese los digitos de su rut antes del guion: "))

a=x%10
b=(x//10)%10
c=(x//100)%10
d=(x//1000)%10
e=(x//10000)%10
f=(x//100000)%10
g=(x//1000000)%10
h=(x//10000000)%10

suma=2*a+3*b+4*c+5*d+6*e+7*f+2*g+3*h
suma=int(suma)
modulo= int (suma//11)
daniel= suma-(11*modulo)

y= 11-daniel

if 0<= y <=9:
    print("dv={}".format(y))
if y==11:
    print("dv=0")
if y==10:
    print("dv=K")
