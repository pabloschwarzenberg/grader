#Cálculo del dígito verificador de un rut
rut = input("Ingresar el rut sin el numero verificador: ")

inverso = rut[len(rut)::-1]
suma = 0
contador = 2

for a in inverso:
    suma += int(a) * contador
    contador += 1

    if contador == 8:
        contador = 2

resto = suma % 11

dv = 11 - resto

if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print("dv =", dv)      