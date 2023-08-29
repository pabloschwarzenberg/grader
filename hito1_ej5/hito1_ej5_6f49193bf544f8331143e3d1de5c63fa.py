rut = input('Ingrese su rut: ')
rut_invertido = rut[::-1]
multiplicar = [2, 3, 4, 5, 6, 7, 2, 3]
resultado = list(map(lambda x, y: int(x) * y, rut_invertido, multiplicar))
suma = sum(resultado)
resto = suma % 11
if resto == 1:
    dv = 'k'
elif resto == 0:
    dv = 0
else:
    dv = 11 - resto
print('dv =', dv)
