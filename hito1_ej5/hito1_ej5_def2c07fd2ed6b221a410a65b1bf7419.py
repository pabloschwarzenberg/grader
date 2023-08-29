#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut: "))
a=rut%10
rut=rut//10
b=rut%10
rut=rut//10
c=rut%10
rut=rut//10
d=rut%10
rut=rut//10
e=rut%10
rut=rut//10
f=rut%10
rut=rut//10
g=rut%10
rut=rut//10
h=rut
x=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3
y=x%11
z=11-y
if z==11:
    print("dv=0")
if z==10:
    print("dv=K")
if 1<=z<10:
    str(z)
    print("dv=",z)
     