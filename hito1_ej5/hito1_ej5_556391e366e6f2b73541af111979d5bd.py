rut = input("Ingrese el número de RUT sin el dígito verificador: ")

# Cálculo del dígito verificador
rut_reverso = rut[::-1]
factor = 2
suma = 0

for i in rut_reverso:
    suma += int(i) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)
if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "k"

print("dv =", dv)
