def substring(s,n) :
    x = 0
    y = int(n)
    substrings = []
    while y <= len(s):
        secuencia = s[x : y]
        substrings.append(secuencia)
        x += 1
        y += 1
    return substrings
def substring_final(a) :
    x = 0
    contador = 0
    subsecuencias = []
    while x < len(a) :
        contador_1 = a.count(a[x])
        if contador_1 == 1 :
            contador += 1
            subsecuencias.append(a[x])
        x += 1
    if contador != 0 :
        for numero in range(len(subsecuencias) - 1):
            print(subsecuencias[numero].strip("'"))
        return subsecuencias[len(subsecuencias) - 1]
    if contador == 0 :
        return "ninguna"
s = input()
n = input()
a = substring(s,n)
print(substring_final(a))      