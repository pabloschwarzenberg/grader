def buscarTodas(a, b):
    indices = []
    start = 0
    while True:
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el primer string: ")
    b = input("Ingresa el segundo string: ")
    resultado = buscarTodas(a, b)
    print("Apariciones encontradas en los índices:", resultado)
