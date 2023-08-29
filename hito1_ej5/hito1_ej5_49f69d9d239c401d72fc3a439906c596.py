rut = str(input('Ingresa el Rut: '))
rut_invertido = ''
suma = 0

# invierte el numero de rut
for digito in rut:
    rut_invertido = digito + rut_invertido

serie_numerica = 2

# multiplica los digitos por la serie numerica del 2 al 7, y si sobran digitos, vuelve al principio de la serie
for digito in rut_invertido:
    if 2 <= serie_numerica <= 7:
        suma += int(digito) * serie_numerica
        serie_numerica += 1
    else:
        serie_numerica = 2
        suma += int(digito) * serie_numerica
        serie_numerica += 1

digito_verificador = suma // 11
digito_verificador = suma - (11 * digito_verificador)
digito_verificador = 11 - digito_verificador

if digito_verificador == 11:
    digito_verificador = 0
elif digito_verificador == 10:
    digito_verificador = 'K'

print('dv=', digito_verificador)