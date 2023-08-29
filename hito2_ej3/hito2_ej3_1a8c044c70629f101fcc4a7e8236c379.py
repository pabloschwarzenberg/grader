cadena = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings = set()
repetidos = set()

for i in range(len(cadena) - n + 1):
    substring = cadena[i:i+n]
    if substring in substrings:
        repetidos.add(substring)
    else:
        substrings.add(substring)

unicos = substrings - repetidos

if len(unicos) > 0:
    for substring in unicos:
        print(substring)
else:
    print("ninguna")
    