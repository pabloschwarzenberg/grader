def buscarTodas(a, b):
    indices = []
    indice = a.find(b)
    while indice != -1:
        indices.append(str(indice))
        indice = a.find(b, indice + 1)
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("El resultado es:", resultado)

           