def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)

    for i in range(len(a) - longitud_b + 1):
        if a[i:i + longitud_b] == b:
            indices.append(str(i))

    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el texto a buscar: ")
    b = input("Ingresa el texto a encontrar: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices encontrados:", resultado)

           