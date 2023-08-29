#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
    pass
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: palabras iguales
    if palabra1 == palabra2:
        return "0D"

    # Caso base: palabras con diferencia de longitud de 1
    if abs(m - n) == 1:
        return "IB"

    # Caso base: palabras con diferencia de longitud mayor a 1
    if abs(m - n) > 1:
        return "+1"

    # Caso base: palabras de la misma longitud con distancia de 1
    distancia = sum(1 for a, b in zip(palabra1, palabra2) if a != b)
    if distancia == 1:
        return "1S"

    # Caso base: palabras de la misma longitud con distancia mayor a 1
    return "+1"


if __name__ == "__main__":
    # Ejemplos de uso
    print(levenshtein("gato", "gatito"))  # +1
    print(levenshtein("hola", "ola"))  # IB
    print(levenshtein("gallina", "gallina"))  # 0D
    print(levenshtein("caro", "cara"))  # 1S