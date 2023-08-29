def buscarTodas(a, b):
    # Implementa la lógica para buscar las apariciones de b en a
    indices = []
    longitud_b = len(b)
    indice = 0

    while indice < len(a):
        if a[indice:indice+longitud_b] == b:
            indices.append(str(indice))
            indice += longitud_b
        else:
            indice += 1

    return ' '.join(indices)

if _name_ == "_main_":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Los índices encontrados son:", resultado)