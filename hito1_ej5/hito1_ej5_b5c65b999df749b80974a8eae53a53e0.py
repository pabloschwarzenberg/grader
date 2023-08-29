#Cálculo del dígito verificador de un rut
rut = input("Ingrese el RUT sin dígito verificador: ")

# Verificar si el RUT tiene al menos un dígito
if len(rut) == 0:
    print("El RUT no puede estar vacío.")
    exit()

# Verificar si el RUT contiene solo dígitos
if not rut.isdigit():
    print("El RUT debe contener solo dígitos numéricos.")
    exit()

# Calcular el dígito verificador
rut_reverso = rut[::-1]  # Invertir el orden del RUT
factor = 2
suma = 0

for d in rut_reverso:
    suma += int(d) * factor
    factor = factor + 1 if factor < 7 else 2

dv = 11 - (suma % 11)
dv = str(dv) if dv != 10 else "k"  # Si el resultado es 10, el dígito verificador es "k"
dv = str(dv) if dv != 11 else "0"  # Si el resultado es 11, el dígito verificador es 0

print("dv =", dv)