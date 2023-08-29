def buscarTodas(a, b):
    indices = []

    index = a.find(b)
    while index != -1:
        indices.append(str(index))
        index = a.find(b, index + 1)

    resultado = ' '.join(indices)

    return resultado


if __name__ == "__main__":
    cadena_a = input("Ingresa una cadena: ")
    cadena_b = input("Ingresa el substring a buscar: ")

    resultado = buscarTodas(cadena_a, cadena_b)
    print(resultado)