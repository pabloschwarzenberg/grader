#Cálculo del dígito verificador de un rut
rut = int(input("Ingresa el rut sin dígito verificador: "))
rut_str = str(rut)
multiplicadores = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rut_str)-1, -1, -1):
    digito = int(rut_str[i])
    multiplicador = multiplicadores[(len(rut_str)-1-i) % 6]
    suma += digito * multiplicador

resto = suma % 11
dv = 11 - resto

if dv == 10:
    digito_verificador = 'k'
elif dv == 11:
    digito_verificador = '0'
else:
    digito_verificador = str(dv)

print("dv=" + digito_verificador)      