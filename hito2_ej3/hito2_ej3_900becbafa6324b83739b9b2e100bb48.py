 def obtener_strings_unicos(secuencia, n):
    strings = []
    contador = {}

    for i in range(len(secuencia) -n +1 ):
        string = secuencia[i:i+n]

        if string in contador:
            contador[string] += 1
        else:
            contador[string] = 1

    for string, count in contador.items():
        if count == 1:
            strings.append(string)

    return strings


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el valor de n: "))

    resultados = obtener_strings_unicos(secuencia, n)

    if len(resultados) > 0:
        for resultado in resultados:
            print(resultado)
    else:
        print("ninguna")    