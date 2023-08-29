#Cálculo del dígito verificador de un rut
rut = input('Ingrese rut: ')
i = 2
suma_rut = 0
for numero in rut[::-1]:
    if i == 8:
        i = 2
    suma_rut += int(numero) * i
    i += 1
division = suma_rut % 11
digito_ver = 11- division
if digito_ver == 11:
    digito_ver = 0
elif digito_ver == 10:
    digito_ver = 'K'
print('dv=' + str(digito_ver))