secuencia = str(input(""))
secuencia = secuencia.upper()
for i in secuencia:
    if i == "A":
        secuencia = True
        print("correcta")
    elif i == "T":
        secuencia = True
        print("correcta")
    elif i == "C":
        secuencia = True
        print("correcta")
    elif i == "G":
        secuencia = True
        print ("correcta")
    else:
        secuencia = False
        print ("incorrecta")