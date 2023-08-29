secuencia = input("Ingrese la secuencia: ")

valida = True
for c in secuencia:
    if c.upper() not in "ACTG":
        valida = False
        break

if valida:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
    