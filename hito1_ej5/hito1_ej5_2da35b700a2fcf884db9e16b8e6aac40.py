#Cálculo del dígito verificador de un rut
rut = input("Ingrese Rut ")
i = len(rut) - 1
rutInvertido = ""
while i >= 0:
    rutInvertido = rutInvertido + rut[i]
    i -= 1

listaRut = list(rutInvertido)
multiplicador = 2
sumaDigitos = 0
for digito in listaRut:
    sumaDigitos = sumaDigitos + (int(digito) * multiplicador)
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = int(sumaDigitos / 11)
restoDivision = sumaDigitos - (11 * resto)
dv = 11 - restoDivision
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"
print("dv="+str(dv))
