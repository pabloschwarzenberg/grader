#Cálculo del dígito verificador de un rut
rut = int(input('Ingrese rut(sin puntos): '))

suma = 0
num = 2
i = 0

rut_invertido = str(rut)[::-1]
while i < len(rut_invertido):
    if num > 7:
        num = 2

    suma += int(rut_invertido[i]) * num
    num += 1
    i += 1

modulo = suma % 11
ver = 11 - modulo

if ver == 11:
    print('dv=0')

elif ver == 10:
    print('dv=K')

else:
    print('dv=' + str(ver))     