def buscarTodas(a, b):
    indices = []
    indice = -1
    
    while True:
        indice = a.find(b, indice + 1)
        if indice == -1:
            break
        indices.append(str(indice))
    
    return ' '.join(indices)

# Ejemplo de uso
texto = "tres tristes tigres"
subtexto = "t"
indices_encontrados = buscarTodas(texto, subtexto)
print(indices_encontrados)
