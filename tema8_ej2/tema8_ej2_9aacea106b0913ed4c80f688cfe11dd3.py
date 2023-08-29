def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)

    for i in range(len(a)):
        if a[i:i+longitud_b] == b:
            indices.append(str(i))

    return ' '.join(indices)

if __name__ == "__main__":
    texto = input("Ingresa el texto: ")
    buscar = input("Ingresa la secuencia a buscar: ")

    resultado = buscarTodas(texto, buscar)
    print(resultado)
