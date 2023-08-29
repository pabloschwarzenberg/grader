#Cálculo del dígito verificador de un rut
    # Solicitar el número del RUT al usuario
rut = input("Ingrese el número del RUT (sin puntos ni dígito verificador): ")

# Calcular el dígito verificador
rut_reverso = rut[::-1]
factor = 2
suma = 0

for digito in rut_reverso:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

dv = 11 - (suma % 11)
if dv == 10:
    dv = 'K'
elif dv == 11:
    dv = '0'

# Imprimir el resultado
print("dv =", dv)
