#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut sin numero verificador: ")
rut = rut[::-1]
suma = 0
multiplicador = 2
for digito in rut:
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2
resto = suma % 11
dv = 11 - resto
if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'
x = ("dv=")
print(x,dv)    