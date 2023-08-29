cadena = str(input("Ingrese cadena: "))
n = int(input("Ingrese el largo: "))
substrings = []
i = len(cadena)
while i > 0:
    substring = cadena[0:i]
    substrings.append(substring)
    l = 0
    while l < i:
        substring2 = substring[l:i]
        if substring2 == substring:
            l += 1
            continue
        else:
            substrings.append(substring2)
            l += 1
    i -= 1
substrings_largo_n = []
for elemento in substrings:
    if len(elemento) == n:
        substrings_largo_n.append(elemento)
substrings_unicos = []
for elemento in substrings_largo_n:
    if substrings_largo_n.count(elemento) == 1:
        substrings_unicos.append(elemento)
if len(substrings_unicos) == 0:
    print("ninguna")
else:
    string_a_retornar = ""
    for elemento in substrings_unicos:
        print(elemento)

  