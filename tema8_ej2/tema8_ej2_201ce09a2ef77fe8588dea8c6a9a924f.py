def buscarTodas(a, b):
    indices = []
    index = -1
    while True:
        index = a.find(b, index + 1)
        if index == -1:
            break
        indices.append(str(index))
    return ' '.join(indices)

texto = input("Ingrese el texto: ")
palabra = input("Ingrese la palabra a buscar: ")
resultado = buscarTodas(texto, palabra)
print("Índices de apariciones:", resultado)
