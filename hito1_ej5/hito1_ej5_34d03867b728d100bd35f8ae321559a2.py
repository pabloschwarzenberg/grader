#Cálculo del dígito verificador de un rut
      # Pedir al usuario que ingrese el número del RUT sin el dígito verificador
numero_rut = input("Ingrese el número del RUT sin el dígito verificador: ")

# Calcular el dígito verificador utilizando el algoritmo del RUT
suma = 0
multiplicador = 2

for digito in reversed(numero_rut):
    suma += int(digito) * multiplicador
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
dv = 11 - resto

# Manejar el caso especial del dígito verificador igual a 11
if dv == 10:
    dv = "k"
elif dv == 11:
    dv = 0

# Imprimir el dígito verificador calculado
print("dv =", dv)