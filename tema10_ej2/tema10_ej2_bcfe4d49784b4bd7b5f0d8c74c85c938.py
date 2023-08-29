def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)
    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m
    distancias = range(m + 1)
    for i, letra2 in enumerate(palabra2):
        nuevas_distancias = [i + 1]
        for j, letra1 in enumerate(palabra1):
            if letra1 == letra2:
                nuevas_distancias.append(distancias[j])
            else:
                nuevas_distancias.append(1 + min((distancias[j], distancias[j + 1], nuevas_distancias[-1])))
        distancias = nuevas_distancias
    distancia = distancias[-1]
    if distancia == 0:
        return "0D"
    elif distancia == 1:
        return "IB" if m != n else "1S"
    else:
        return "+1"


if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)           