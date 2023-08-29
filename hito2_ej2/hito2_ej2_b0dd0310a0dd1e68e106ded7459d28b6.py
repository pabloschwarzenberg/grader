secuencia = str(input("Escriba secuencia: ")).upper()
for i in secuencia:
    if not (i == str("A")) or (i == str("C")) or (i == str("T")) or (i == str("G")):
        print("secuencia incorrecta")
    if (i == str("A")) or (i == str("C")) or (i == str("T")) or (i == str("G")):
        print("secuencia correcta")      