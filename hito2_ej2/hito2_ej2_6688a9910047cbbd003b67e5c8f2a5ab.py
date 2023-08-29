secuencia = str(input("Ingrese la secuencia: "))
secuencia.upper()
list(secuencia)
for letra in secuencia:
    if letra == secuencia[-1]:
        if letra != "A" or letra != "C" or letra != "T" or letra != "G":
            print("secuencia incorrecta")
            break
        else:
            print("secuencia correcta")
            break
    if letra != "A" or letra != "C" or letra != "T" or letra != "G":
        print("secuencia incorrecta")
        break