def buscarTodas(a, b):
    indices = []
    index = a.find(b)
    while index != -1:
        indices.append(str(index))
        index = a.find(b, index + 1)
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Indices encontrados:", resultado)

           