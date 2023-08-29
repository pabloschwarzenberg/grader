def buscarTodas(a, b):
    indices = []
    i = 0

    while i < len(a):
        if a[i:i + len(b)] == b:
            indices.append(str(i))
            i += len(b)
        else:
            i += 1

    return ' '.join(indices)


if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    buscar = input("Ingrese el string a buscar: ")
    resultado = buscarTodas(texto, buscar)
    print("Secuencia de índices:", resultado)