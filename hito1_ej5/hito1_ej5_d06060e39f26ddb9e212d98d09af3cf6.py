numero = input("Ingresa tu rut sin el digito verificador: ")

largo = len(numero)

m = 1

suma = 0

for i in range(largo-1,-1,-1):

    m = m + 1

    suma = suma + int(numero[i])*m

    if m == 7:

        m = 1

resto = suma % 11

dv = 11 - resto

dv = str(dv)

if dv == "11":

    dv = "0"

if dv == "10":

    dv = "K"

print("dv=",dv)