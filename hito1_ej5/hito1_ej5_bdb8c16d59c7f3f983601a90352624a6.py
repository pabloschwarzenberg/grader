#Cálculo del dígito verificador de un rut
rut = input("ingrese el rut: ")
multiplo = 2
i = len(rut) -1
suma = 0

while i >= 0:
    suma = suma + (int(rut[i]) * multiplo)
    multiplo = multiplo + 1
    if multiplo == 8:
        multiplo = 2
    i= i - 1

resto = suma % 11
dv = 11- resto

if dv == 11:
    dv = 0
elif dv == 10:
    dv = "k"

print("dv=", dv)      