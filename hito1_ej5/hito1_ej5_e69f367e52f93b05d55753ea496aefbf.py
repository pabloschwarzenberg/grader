#Cálculo del dígito verificador de un rut
rut = int(input('Ingresa tu RUT: '))

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

print(d1, d2, d3, d4, d5, d6, d7, d8)

suma = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 + d2*2 + d1*3
print('suma', suma)

resto = suma%11
print('resto', resto)

resultado = 11 - resto

if resultado == 11:
    print('dv=0')

if resultado == 10:
    print('dv=k')

if resultado !=10 and resultado !=11:
    print('dv=',resultado)            