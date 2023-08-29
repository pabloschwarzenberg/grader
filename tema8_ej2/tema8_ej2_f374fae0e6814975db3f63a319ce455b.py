def buscarTodas(a, b):
    indices = []
    inicio = 0
    while inicio < len(a):
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese una cadena a: ")
    b = input("Ingrese una subcadena b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices:", resultado)
        