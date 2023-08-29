#Cálculo del dígito verificador de un rut
rut=int(input('Ingrese rut:'))
a=rut//10000000
a=a*8
rut=rut%10000000
b=rut//1000000
b=b*9
rut=rut%1000000
c=rut//100000
c=c*4
rut=rut%100000
d=rut//10000
d=d*5
rut=rut%10000
e=rut//1000
e=e*6
rut=rut%1000
f=rut//100
f=f*7
rut=rut%100
g=rut//10
g=g*8
rut=rut%10
h=rut//1
h=h*9
suma=a+b+c+d+e+f+g+h
division=suma%11
if division==10:
    print('dv=K')

else:
    print('dv=',division)     