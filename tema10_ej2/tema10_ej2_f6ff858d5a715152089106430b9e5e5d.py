def levenshtein(palabra1,palabra2):

    largo_palabra1 = len(palabra1)
    largo_palabra2 = len(palabra2)

    lista = [[0] * (largo_palabra2 + 1) for _ in range(largo_palabra1 + 1)]

    for i in range(largo_palabra1 + 1):
        lista[i][0] = i
    for x in range(largo_palabra2 + 1):
        lista[0][x] = x
    
    for i in range(1, largo_palabra1 + 1):
        for x in range(1, largo_palabra2 + 1):
            if palabra1[i - 1] == palabra2[x - 1]:
                lista[i][x] = lista[i - 1][x - 1]
            else:
                lista[i][x] = 1 + min(lista[i - 1][x], lista[i][x - 1], lista[i - 1][x - 1])

    distancia = lista[-1][-1]

    if distancia > 1:
        return "+1"

    elif distancia == 0:
        return "0D"
    
    elif ((largo_palabra2 == largo_palabra1) and (distancia == 1)):
        return "1S"
    
    elif distancia == 1:
        return "IB"

if __name__ == "__main__":

    palabra1 = input("Indique la primera palabra: ")
    palabra2 = input("Indique la segunda palabra: ")

    respuesta = levenshtein(palabra1,palabra2)
    print(respuesta)