#Cálculo del dígito verificador de un rut
rut= int(input('Ingrese su rut sin digito verificador: '))
a=((rut%10)*2)
b=(((rut//10)%10)*3)
c=(((rut//100)%10)*4)
d=(((rut//1000)%10)*5)
e=(((rut//10000)%10)*6)
f=(((rut//100000)%10)*7)
g=(((rut//1000000)%10)*2)
h=(((rut//10000000)%10)*3)

suma= a+b+c+d+e+f+g+h
resultado = suma%11
digito = (11-resultado)
if digito == 11:
    print('dv=0')
elif digito == 10:
        print('dv=K')
else:
    print('dv=',digito)