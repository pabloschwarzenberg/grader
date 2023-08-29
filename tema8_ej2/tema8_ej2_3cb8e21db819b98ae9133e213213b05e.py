def buscarTodas(a, b):
    indices = []
    empieza = 0
    while True:
        indice = a.find(b, empieza)
        if indice == -1:
            break
        indices.append(str(indice))
        empieza = indice + 1
    return ' '.join(indices)
    
if __name__ == "__main__":
    pass
           