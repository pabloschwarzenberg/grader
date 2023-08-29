def buscarTodas(a, b):
    indices = []
    indice = 0
    while indice != -1:
        indice = a.find(b, indice)
        if indice != -1:
            indices.append(str(indice))
            indice += 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Los índices de las apariciones son:", resultado)