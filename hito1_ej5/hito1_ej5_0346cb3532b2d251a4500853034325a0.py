
rut = input("Ingrese un número de RUT sin dígito verificador: ")


rut = rut[::-1]  
factor = 2
suma = 0

for digito in rut:
    suma += int(digito) * factor
    factor = factor + 1
    if factor == 8:
        factor = 2

resto = suma % 11
dv = 11 - resto


if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"


print("dv =", dv)    