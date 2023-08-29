def buscarTodas(a,b):
    pass

if __name__ == "__main__":
    pass
def buscarTodas(a, b):
    indices = []

    # Buscar todas las apariciones de b en a
    start = 0
    while True:
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1

    # Retornar los índices como un string separado por espacios
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)
           