#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el RUT sin dígito verificador: "))

rut_str = str(rut)[::-1]
suma = 0
factor = 2

for char in rut_str:
    suma += int(char) * factor
    factor += 1
    if factor > 7:
        factor = 2

modulo = suma % 11
dv = 11 - modulo

if dv == 10:
    dv = "K"
elif dv == 11:
    dv = 0

print("dv=",dv)    