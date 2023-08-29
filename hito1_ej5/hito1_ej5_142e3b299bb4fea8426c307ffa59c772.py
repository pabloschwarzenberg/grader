#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT: ")

invertir=rut[::-1]
suma = 0
multiplo = 2

for digito in (invertir):
    suma+=int(digito)*multiplo
    multiplo+=1
    if (multiplo==8):
        multiplo=2

resto=(suma % 11)
dv=(11 - resto)
if (dv==11):
    dv=0
elif (dv==10):
    dv="K"

print("dv =", dv)      