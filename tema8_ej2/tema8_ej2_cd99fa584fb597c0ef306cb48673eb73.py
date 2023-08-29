def buscarTodas(a, b):
    indices = []
    index = 0
    while index < len(a):
        index = a.find(b, index)
        if index == -1:
            break
        indices.append(str(index))
        index += 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Indices encontrados:", resultado)
