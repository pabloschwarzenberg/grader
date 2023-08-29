def find_unique_substrings(string, n):
    substrings = {}
    unique_substrings = []

#obtenerstrings de largo n
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

#operacion
    for substring, count in substrings.items():
        if count == 1:
            unique_substrings.append(substring)

    return unique_substrings


#ingreso de entradas
string = input("Ingresa un string: ")
n = int(input("Ingresa el valor de n: "))

#encontrar los substrings únicos
unique_substrings = find_unique_substrings(string, n)

#immprimir los substrings únicos encontrados
if unique_substrings:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
      