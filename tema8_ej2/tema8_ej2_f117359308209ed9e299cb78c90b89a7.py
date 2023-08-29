def buscarTodas(a, b):
    indices = []
    start = 0
    while start < len(a):
        index = a.find(b, start)
        if index != -1:
            indices.append(str(index))
            start = index + 1
        else:
            break
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese una cadena de texto: ")
    b = input("Ingrese el substring a buscar: ")
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)
