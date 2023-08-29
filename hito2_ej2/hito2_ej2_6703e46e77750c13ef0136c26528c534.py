genoma = ['A', 'T', 'C', 'G']

seq = input().upper()

valida = True
for letra in seq:
    if not letra in genoma:
        valida = False
        break

if valida:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")   