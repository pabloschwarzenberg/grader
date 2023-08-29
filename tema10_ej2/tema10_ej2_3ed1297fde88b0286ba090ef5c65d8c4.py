def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"  # La distancia es mayor que 1

    if m == n:
        diferencia = sum(p1 != p2 for p1, p2 in zip(palabra1, palabra2))
        if diferencia == 1:
            return "1S"  # La distancia es 1 porque hay que sustituir una letra

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    i = 0
    j = 0
    distancia = 0
    while i < m and j < n:
        if palabra1[i] != palabra2[j]:
            distancia += 1
            if m != n:
                i += 1  # Se corrige aquí, incrementar el índice de palabra1
        i += 1
        j += 1

    if distancia <= 1:
        return "IB"  # La distancia es 1, y para llegar de una palabra a la otra hay que insertar o borrar una letra

    return "+1"  # La distancia es mayor que 1


if __name__ == "__main__":
    resultado = levenshtein("gato", "gatito")
    print(resultado)  # Debería imprimir "+1"

    resultado = levenshtein("hola", "ola")
    print(resultado)  # Debería imprimir "IB"

    resultado = levenshtein("caro", "cara")
    print(resultado)  # Debería imprimir "1S"

    resultado = levenshtein("gallina", "gallina")
    print(resultado)  # Debería imprimir "0D"
    
    resultado = levenshtein("jaron", "jarron")
    print(resultado)  # Debería imprimir "IB"
