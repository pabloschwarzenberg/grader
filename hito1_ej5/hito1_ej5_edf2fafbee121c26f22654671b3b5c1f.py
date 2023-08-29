# Ingresar el número del RUT sin dígito verificador
rut = input("Ingrese el número del RUT (sin guion): ")

# Calcular el dígito verificador
dv = rut[2:]

print(dv)