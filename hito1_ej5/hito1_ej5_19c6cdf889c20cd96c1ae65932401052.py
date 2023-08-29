# Solicitar el número de Rut al usuario
rut = input("Ingrese el número de Rut (sin dígito verificador): ")

# Calcular el dígito verificador utilizando el algoritmo
suma = 0
multiplo = 2

# Recorrer el número de Rut de derecha a izquierda
for i in reversed(rut):
    suma += int(i) * multiplo
    multiplo = (multiplo + 1) % 8 or 2

# Calcular el dígito verificador
resto = suma % 11
dv = 11 - resto

# Si el resto es 0, el dígito verificador es 11
if resto == 0:
    dv = 0
# Si el resto es 1, el dígito verificador es 'k'
elif resto == 1:
    dv = 'k'

# Imprimir el resultado
print("dv =", dv)

#FIN