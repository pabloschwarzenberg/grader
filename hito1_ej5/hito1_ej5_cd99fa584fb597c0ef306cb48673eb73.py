#Cálculo del dígito verificador de un rut
rut = input("Ingrese un número de rut: ")

# Inicializar variables
factor = 2
suma = 0

# Calcular la suma ponderada
for i in range(len(rut)-1, -1, -1):
    suma += int(rut[i]) * factor
    factor = (factor + 1) % 8 or 2

# Calcular el dígito verificador
dv = (11 - (suma % 11)) % 11

print("dv =", dv)
