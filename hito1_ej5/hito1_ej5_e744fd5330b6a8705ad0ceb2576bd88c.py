#Cálculo del dígito verificador de un rut
rut=eval(input('ingrese rut sin guion:'))
d8=rut%10
rut=rut//10
d7=rut%10
rut=rut//10
d6=rut%10
rut=rut//10
d5=rut%10
rut=rut//10
d4=rut%10
rut=rut//10
d3=rut%10
rut=rut//10
d2=rut%10
rut=rut//10
d1=rut%10
suma=((d8*2)+(d7*3)+(d6*4)+(d5*5)+(d4*6)+(d3*7)+(d2*2)+(d1*3))
x=suma//11
lol=suma-(11*x)
dv=11-lol

if dv==11:
    print('dv=0')
if dv==10:
    print('dv=k')
if dv==dv:
    print('dv=',dv)