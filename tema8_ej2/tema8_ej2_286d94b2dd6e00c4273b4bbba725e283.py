def buscarTodas(a, b):
    indices = []
    index = -1

    while True:
        index = a.find(b, index + 1)
        if index == -1:
            break
        indices.append(str(index))

    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Indices encontrados:", resultado)
