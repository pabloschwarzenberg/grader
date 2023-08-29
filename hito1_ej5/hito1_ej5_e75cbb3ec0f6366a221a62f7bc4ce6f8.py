rut = []
ingreso = input('Ingrese su RUT: ')
for x in ingreso:
    rut.append(x)
rut.reverse()
inicio = 2
multiplicacion = 0
for a in rut:
    multiplicacion += int(a) * inicio
    if inicio == 7:
        inicio = 2
    else:
        inicio += 1
entero = multiplicacion // 11
mod = multiplicacion - (11*entero)
final = 11 - mod
if final == 11:
    digito = 0
elif final == 10:
    digito = "K"
else:
    digito = final
print('dv=',digito)
