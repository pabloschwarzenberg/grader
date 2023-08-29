#Cálculo del dígito verificador de un rut
rut = input("Ingresa el RUT sin dígito verificador: ")

# Calcular el dígito verificador
factor = 2
suma = 0
for i in reversed(rut):
    suma += int(i) * factor
    factor += 1
    if factor > 7:
        factor = 2
dv = 11 - (suma % 11)

# Imprimir el resultado
if dv == 11:
    print("dv=0")
elif dv == 10:
    print("dv=k")
else:
    print("dv=", dv)
      