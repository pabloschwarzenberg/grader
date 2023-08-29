def levenshtein(palabra1, palabra2):
    diferencia = 0
    a = list(palabra1)
    b = list(palabra2)
    if len(palabra1) > len(palabra2):
        for i in range(len(b)):
            if b[i] not in a:
                diferencia += 1
        for i in range(len(a)-len(b)):
            diferencia += 1

    if len(palabra2) > len(palabra1):
        for i in range(len(a)):
            if a[i] not in b:
                diferencia += 1
        for i in range(len(b)-len(a)):
            diferencia += 1
    if len(palabra2) == len(palabra1):
        for i in range(len(a)):
            if a[i] not in b:
                diferencia += 1

    if diferencia == 0:
        return ("0D")
    if diferencia > 1:
        return("+1")
    if diferencia == 1 and len(a) == len(b):
        return("1S")
    if diferencia == 1 and len(a) != len(b):
        return("IB")
if __name__ == "__main__":
    palabra1 = str(input())
    palabra2 = str(input())
    print(levenshtein(palabra1, palabra2))