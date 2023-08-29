# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1, palabra2):
    c = 0
    d = 0
    e = 0
    pal1 = []
    pal2 = []
    for letr in palabra1:
        c += 1
        pal1.append(letr)
    for letra in palabra2:
        d += 1
        pal2.append(letra)
    if pal1 != pal2 and c == d:
        return "1S"
    if palabra1 == palabra2:
        return "0D"
    if pal1[0] != pal2[0]:
        return "+1"
    else:
        c -= d
        if c == 1 or c == -1:
            return "IB"
        if c > 1 or c < -1:
            return "+1"


if __name__ == "__main__":
    a = input()
    b = input()
    print(levenshtein(a, b))
    pass
           