#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    uno = len(palabra1)
    dos = len(palabra2)

    m = [[0] * (dos + 1) for _ in range(uno + 1)]

    for i in range(uno + 1):
        m[i][0] = i
    for j in range(dos + 1):
        m[0][j] = j

    for i in range(1, uno + 1):
        for j in range(1, dos + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1

    dis = m[uno][dos]
    if dis > 1:
        return "+1"
    elif dis == 1:
        if uno == dos:
            return "1S"
        else:
            return "IB"
    elif dis == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
