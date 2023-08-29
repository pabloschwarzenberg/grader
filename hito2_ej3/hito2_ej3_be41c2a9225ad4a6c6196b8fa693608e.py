def encontrar_substrings_unicos(secuencia, n):
    conteo_substrings = {}

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]

        if substring in conteo_substrings:
            conteo_substrings[substring] += 1
        else:
            conteo_substrings[substring] = 1

    substrings_unicos = [substring for substring, conteo in conteo_substrings.items() if conteo == 1]

    return substrings_unicos

secuencia = input()
n = int(input())

substrings_unicos = encontrar_substrings_unicos(secuencia, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      