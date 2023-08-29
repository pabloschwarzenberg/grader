#Cálculo del dígito verificador de un rut
rut = input('Ingrese el rut sin digito verificador: ')
rut_invertido = ''
for numero in rut:
    rut_invertido = numero + rut_invertido
print(rut_invertido)

multiplicacion = 0
i = 2
for numero in rut_invertido:
    multiplicacion += int(numero) * i
    i+=1
    if i>7:
        i=2

division = multiplicacion % 11
dv = 11-division
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'k'
print('dv={}'.format(dv))