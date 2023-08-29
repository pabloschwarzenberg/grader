def validar(ADN, ADN_2):
    ADN = ADN.upper()
    ADN_2 = ADN_2.upper()
    secuencia = largo(ADN, ADN_2)
    return secuencia
def largo(ADN, n):
    alinear = ""
    for i in range(len(n)):
        letra = n[i]
        print(letra)
        print(ADN)
        if ADN == "":
            break
        for j in range(len(ADN)):
            letra_2 = ADN[j]
            print(letra_2)
            if letra_2 == "_":
                pass
            elif letra_2 == letra:
                alinear += n[i]
                ADN = ADN.replace(letra_2, "", 1)
                n = n.replace(letra, "_", 1)
                print(n)
                break
            else:
                ADN = ADN.replace(letra_2, "_", 1)
                alinear += "_"
        ADN = ADN.replace("_", "")
    n = n.replace("_", "")
    if ADN == "":
        alinear += n
    alineados = alinear
    return alineados
ADN = input()
ADN_2 = input()
print(validar(ADN, ADN_2))      