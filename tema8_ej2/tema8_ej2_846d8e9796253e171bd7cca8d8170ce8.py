def buscarTodas(a, b):
    indices = []
    start = 0
    while True:
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)


if __name__ == "__main__":
    a = input("Ingresa el texto a buscar: ")
    b = input("Ingresa el texto a encontrar: ")
    resultado = buscarTodas(a, b)
    print("Los índices encontrados son:", resultado)
