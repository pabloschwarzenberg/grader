def buscarTodas(a, b):
    indices = []
    start = 0
    while start < len(a):
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)

if __name__ == "__main__":
    cadena_a = input("Ingrese una cadena a: ")
    cadena_b = input("Ingrese una cadena b: ")
    resultado = buscarTodas(cadena_a, cadena_b)
    print("Índices encontrados:", resultado)

           