def buscarTodas(a, b):
    indices = []
    pos = 0
    while True:
        index = a.find(b, pos)
        if index == -1:
            break
        indices.append(str(index))
        pos = index + 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Apariciones encontradas en los índices:", resultado)

