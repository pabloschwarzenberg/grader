def secuencia(arn):
    contador = 1
    while contador == 1:
        for i in range (len(arn)):
            if (arn[i] == "A" or arn[i] == "C" or arn[i] == "T" or arn[i] == "G" or arn[i] == "a" or arn[i] == "c" or arn[i] == "t" or arn[i] == "g"):
                na_error = ""
            else:
                print("secuencia incorrecta", end="")
                contador = 0
                break
        if (contador == True):
            inicio = "ACTG"
            final = "TGAC"
            palabra_if = dict(zip(inicio + final, final + inicio))
            x = "".join(palabra_if.get(x.upper(), x) for x in arn)
            print("secuencia correcta", end="")
            return x.lower()
            pass
    return na_error


arn= input("Ingresa la secuencia del Genoma, solo ( A, C, T, G): ")
print(secuencia(arn), end="")