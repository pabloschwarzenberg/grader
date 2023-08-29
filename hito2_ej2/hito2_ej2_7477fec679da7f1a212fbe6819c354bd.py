def Verificaion_ADN (y):
    validador=True
    y=y.upper()
    for i in range(0,len(y)):
        if y[i] != "C" and y[i] != "A" and y[i] != "T" and y[i] != "G":
            validador = False
            break
    if validador == True:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
    return

print(Verificaion_ADN(input("Ingrese secuencia: ").upper()))