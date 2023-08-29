def buscarTodas(a, b):
    indices = []
    inicio = 0
    while inicio < len(a):
        indice = a.find(b, inicio)
        if indice != -1:
            indices.append(str(indice))
            inicio = indice + 1
        else:
            break
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el primer string: ")
    b = input("Ingrese el segundo string: ")
    resultado = buscarTodas(a, b)
    print("Resultado:", resultado)
