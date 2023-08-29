entrada = input()
entrada = entrada.upper()
cont = 0
for x in entrada:
    if x != "A" and x != "C" and x != "T" and x != "G":
        cont += 1
if cont != 0:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")
