ADN_correctos = ["A", "C", "T", "G"]
def validar(ADN):
    ADN = ADN.upper()
    if comparar(ADN):
        secuencia = "secuencia correcta"
    else:
        secuencia = "secuencia incorrecta"
    return secuencia
def comparar(ADN):
    iguales = len(ADN)
    distintos = 0
    for i in ADN:
        for j in ADN_correctos:
            print("ADN", i, "Comparando con", j)
            if i == j:
                distintos += 1
                break
    print(distintos, iguales)
    if distintos == iguales:
        return True
    else:
        return False


ADN = input()
print(validar(ADN))      