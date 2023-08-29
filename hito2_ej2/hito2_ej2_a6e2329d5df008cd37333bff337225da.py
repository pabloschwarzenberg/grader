secuencia = input()
x = True
genoma = ["A", "C", "T", "G"]
for letra in secuencia:
    if letra.upper() in genoma:
        pass
    else:
        x = False
        break
if x:
    print ("secuencia correcta")
else:
    print("secuencia incorrecta")