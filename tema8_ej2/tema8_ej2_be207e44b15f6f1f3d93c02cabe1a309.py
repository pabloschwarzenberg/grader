def buscarTodas(a,b):
    resultado = ""
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            resultado += str(i) + " "
    return resultado[:-1]
