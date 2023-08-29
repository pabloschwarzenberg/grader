rut = input("Ingrese el RUT (sin dígito verificador): ")

rutalreves = rut[::-1]
factor = 2
suma = 0

for i in rutalreves:
    suma += int(i) * factor
    factor = 2 if factor == 7 else factor + 1

resto = suma % 11
dv = 11 - resto if resto != 0 else 0

if dv == 10:
    dv = "k"

print("dv =", dv)
