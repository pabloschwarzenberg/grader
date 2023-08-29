def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    if palabra1 == palabra2:
        return "0D"

    if abs(m - n) > 1:
        return "+1"

    if m == n:
        distancia = sum(a != b for a, b in zip(palabra1, palabra2))
        if distancia == 1:
            return "1S"

    return "IB"


if __name__ == "__main__":
    palabras = [("gato", "gatito"), ("hola", "ola"), ("gallina", "gallina"), ("caro", "cara")]
    for palabra1, palabra2 in palabras:
        resultado = levenshtein(palabra1, palabra2)
        print(f"Palabra 1: {palabra1}")
        print(f"Palabra 2: {palabra2}")
        print(f"Resultado: {resultado}")
        print()

