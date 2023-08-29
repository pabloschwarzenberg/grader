def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            nuevo_caracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            nuevo_caracter = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado

#FUNCION BUSCARTODAS
def buscarTodas(a, b):
    indices = []
    inicio = 0
    while True:
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)
           