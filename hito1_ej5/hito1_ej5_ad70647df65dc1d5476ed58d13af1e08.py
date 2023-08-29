#Cálculo del dígito verificador de un rut
rut = input("Ingrese el número de RUT (sin puntos ni guión): ")

factor = 2
suma = 0

for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = suma % 11
if resto == 1:
    digito_verificador = 'K'
elif resto == 0:
    digito_verificador = '0'
else:
    digito_verificador = 11 - resto

print("dv =", digito_verificador)
