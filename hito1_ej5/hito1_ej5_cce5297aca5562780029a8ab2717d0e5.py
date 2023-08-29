# Solicitar rut al usuario
rut = input("Ingrese un rut (sin dígito verificador): ")

# Verificar que el rut sea válido
if not rut.isdigit() or len(rut) < 1:
    print("Rut inválido")
    exit()

# Calcular dígito verificador
factor = 2
suma = 0

for i in range(len(rut)-1, -1, -1):
    suma += int(rut[i]) * factor
    factor = factor + 1 if factor < 7 else 2

dv = 11 - (suma % 11)
dv = str(dv) if dv != 10 else '0'

# Imprimir resultado
print("dv=" + dv)