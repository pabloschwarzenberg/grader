def buscarTodas(a,b):
    pass

if __name__ == "__main__":
    pass

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
    texto = 'tres tristes tigres'
    subtexto = 't'
    resultado = buscarTodas(texto, subtexto)
    print(resultado)
