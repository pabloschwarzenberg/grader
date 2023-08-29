def buscarTodas(a, b):
    indices = []
    pos = a.find(b)
    while pos != -1:
        indices.append(str(pos))
        pos = a.find(b, pos + 1)
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el texto a: ")
    b = input("Ingresa el texto b: ")
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)
