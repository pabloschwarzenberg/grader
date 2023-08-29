def encontrar_substrings(s, n):
    substrings = set()
    count = {}

    # Generar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    # Encontrar los substrings únicos
    for substring, frequency in count.items():
        if frequency == 1:
            substrings.add(substring)

    return substrings

if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))

    unique_substrings = encontrar_substrings(s, n)

    if len(unique_substrings) == 0:
        print("ninguna")
    else:
        for substring in unique_substrings:
            print(substring)
