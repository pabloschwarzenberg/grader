#Cálculo del dígito verificador de un rut
x=int(input('Ingrese su rut sin el digito verificador: '))
a=(x//10000000)
b=(x//1000000)%10
c=(x//100000)%10
d=(x//10000)%10
e=(x//1000)%10
f=(x//100)%10
g=(x//10)%10
h=x%10

suma =(h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3)
division = suma//11
multiplicacion=division*11
resto= suma-multiplicacion
resto2= suma -(11*division)
dv = 11 - resto2

if dv == 11:
    print('dv=0')
elif dv == 10:
    print('dv=k ')
else:
    print('dv=',dv)     