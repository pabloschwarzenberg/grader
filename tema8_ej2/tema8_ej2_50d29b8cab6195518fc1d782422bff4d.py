def buscarTodas(a, b):
    indices = []
    pos = -1

    # Buscar todas las apariciones de b en a
    while True:
        pos = a.find(b, pos + 1)
        if pos == -1:
            break
        indices.append(str(pos))

    # Unir los índices en un solo string separado por espacios
    resultado = " ".join(indices)

    return resultado

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices: ", resultado)

           