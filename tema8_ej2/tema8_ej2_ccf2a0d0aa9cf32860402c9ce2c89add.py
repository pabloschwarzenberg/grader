def buscarTodas(a, b):
    indices = []
    index = a.find(b)
    while index != -1:
        indices.append(str(index))
        index = a.find(b, index + 1)
    return ' '.join(indices)

if __name__ == "__main__":
    texto_a = input("Ingrese el texto a: ")
    texto_b = input("Ingrese el texto b: ")
    resultado = buscarTodas(texto_a, texto_b)
    print("Secuencia de índices:", resultado)