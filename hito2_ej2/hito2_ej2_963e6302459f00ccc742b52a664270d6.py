def Verificaion_ADN (x):
    valido=True
    x=x.upper()
    for i in range(0,len(x)):
        if x[i] != "C" and x[i] != "A" and x[i] != "T" and x[i] != "G":
            valido = False
            break
    if valido == True:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
    return
print(Verificaion_ADN(input("Ingrese secuencia: ").upper()))