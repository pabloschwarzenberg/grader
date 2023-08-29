#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin dígito verificador): ")


reversed_rut = rut[::-1]  
multiplier = 2
total = 0

for digit in reversed_rut:
    total += int(digit) * multiplier
    multiplier += 1
    if multiplier > 7:
        multiplier = 2

remainder = total % 11
verifier = 11 - remainder


if verifier == 11:
    dv = "0"
elif verifier == 10:
    dv = "K"
else:
    dv = str(verifier)


print("dv =", dv)