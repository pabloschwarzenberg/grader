 def obtenerSubstringsUnicos(s, n):
    substrings = {}
    resultados = []

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    for substring, count in substrings.items():
        if count == 1:
            resultados.append(substring)

    return resultados

entrada = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

substrings = obtenerSubstringsUnicos(entrada, n)

if len(substrings) > 0:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")
