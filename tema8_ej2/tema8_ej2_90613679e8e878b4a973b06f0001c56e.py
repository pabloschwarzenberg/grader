def buscarTodas(a, b):
    posiciones = []
    reemplazo = " "
    for letra in a:
        if letra in b:
            posiciones.append(a.index(letra))
            a = a.replace(letra, reemplazo, 1)
    resultado = (str(posiciones)).strip("[]")
    resultado_final = resultado.replace(",", "")
    return resultado_final




