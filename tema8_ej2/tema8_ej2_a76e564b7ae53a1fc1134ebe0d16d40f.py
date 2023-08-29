def buscarTodas(a, b):
    indices = []
    pos = a.find(b)
    while pos != -1:
        indices.append(str(pos))
        pos = a.find(b, pos + 1)
    return ' '.join(indices)

if __name__ == "__main__":
    texto = input("Ingresar el texto: ")
    subtexto = input("Ingresar el subtexto a buscar: ")
    resultado = buscarTodas(texto, subtexto)
    print("Apariciones en los índices:", resultado)
          