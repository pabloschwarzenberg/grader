def levenshtein(a, b):
    sem = 0
    if len(a) == len(b):
        for letra in a:
            if letra in b:
                sem += 1
                b = b.replace(letra, "", 1)
                d = len(b) - sem
                c = 0
    else:
        for letra in a:
            if letra in b:
                sem += 1
                b = b.replace(letra, "", 1)
                c = len(b) - sem
                d = 0

    return c, d


if __name__ == "__main__":
    p1 = input("Ingrese palabra a comparar:")
    p2 = input("Ingrese palabra a comparar:")
    x, y = levenshtein(p1, p2)
    if x > 1:
        print("+1")
    elif x == 0 and x > y:
        print("IB")
    elif y == 0:
        print("1S")
    elif a == b:
        print("OD")
           