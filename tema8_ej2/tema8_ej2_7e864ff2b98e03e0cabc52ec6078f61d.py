def buscarTodas(a,b):
    resultado = []
    posicion = 0
    for i in a:
        if i == b:
            resultado.append(str(posicion) + " ")
        posicion +=1
    final = "".join(resultado)
    final2 = final[ :-1]
    return final2
