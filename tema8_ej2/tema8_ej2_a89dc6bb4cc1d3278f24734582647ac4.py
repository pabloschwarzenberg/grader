def buscarTodas(a, b):
    indices = []
    index = 0
    while index != -1:
        index = a.find(b, index)
        if index != -1:
            indices.append(str(index))
            index += 1
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Resultado:", resultado)
