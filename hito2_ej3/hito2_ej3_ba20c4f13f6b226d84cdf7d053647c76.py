texto = input("Ingrese el texto: ")
n = int(input("Ingrese el largo de los substrings: "))

substrings = {}
for i in range(len(texto) - n + 1):
    substring = texto[i:i+n]
    if substring in substrings:
        substrings[substring] += 1
    else:
        substrings[substring] = 1

unicos = [k for k, v in substrings.items() if v == 1]

if len(unicos) == 0:
    print("ninguna")
else:
    for substring in unicos:
        print(substring)    