#Cálculo del dígito verificador de un rut
numero_rut = input("Ingrese el número de rut (sin dígito verificador): ")
rut_sin_dv = int(numero_rut)
dv = ""
multiplicador = 2
suma = 0

while rut_sin_dv > 0:
    digito = rut_sin_dv % 10
    suma += digito * multiplicador
    rut_sin_dv = rut_sin_dv // 10
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
if resto == 1:
    dv = "k"
elif resto == 0:
    dv = "0"
else:
    dv = str(11 - resto)

print("dv =", dv)
