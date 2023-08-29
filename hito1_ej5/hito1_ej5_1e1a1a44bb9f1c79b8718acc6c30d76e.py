#Cálculo del dígito verificador de un rut
rut = int(input('Ingresa rut sin puntos ni dígito verificador: '))

d8 = rut%10
rut = rut//10

d7 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d2 = rut%10
rut = rut//10

d1 = rut%10
rut = rut//10

suma = (d1*3 + d2*2 + d3*7 + d4*6 + d5*5 + d6*4 + d7*3 + d8*2)%11
digito = 11 - suma

if digito == 10:
    print('dv=k')
elif digito == 11:
    print('dv=0')
else:
    print('dv=',digito)
    
      