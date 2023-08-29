def verificar(secuencia):
    bases = "CGTA"
    for i in range(len(secuencia)):
        if secuencia[i] not in bases:
            return print("secuencia incorrecta")
    else:
        return print("secuencia correcta")


a = str(input())
verificar(a)