def buscarTodas(a, b):
    indices = []
    length_a = len(a)
    length_b = len(b)
    start = 0

    while start <= length_a - length_b:
        if a[start:start + length_b] == b:
            indices.append(str(start))
        start += 1

    return ' '.join(indices)


if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultados = buscarTodas(a, b)
    print("Indices encontrados:", resultados)
