# Solicitar el número de RUT al usuario
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Cálculo del dígito verificador
rut_reverso = rut[::-1]  # Invertir el RUT
factor = 2
suma = 0

for digito in rut_reverso:
    suma += int(digito) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = suma % 11
dv = 11 - resto

# Casos especiales: si el resto es 0, el dígito verificador es 0.
# Si el resto es 1, el dígito verificador es 'K'.
if resto == 0:
    dv = '0'
elif resto == 1:
    dv = 'K'

# Imprimir el resultado
print("dv =", dv)
