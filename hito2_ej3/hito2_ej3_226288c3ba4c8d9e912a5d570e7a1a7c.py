def obtener_substrings_unicos(texto, n):
    substrings = set()
    for i in range(len(texto) - n + 1):
        substring = texto[i:i+n]
        if texto.count(substring) == 1:
            substrings.add(substring)
    return substrings

if __name__ == "__main__":
    texto = input("Ingrese el texto: ")
    n = int(input("Ingrese el valor de n: "))
    substrings_unicos = obtener_substrings_unicos(texto, n)
    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")