def levenshtein(a, b):
    if (a==b):
        return "0D"
    distancia = 0
    if (len(a)==len(b)):
        for i in range(0,len(a)):
            if(a[i]!= b[i]):
                distancia += 1
        if (distancia == 1):
            return "1S"
    else:
        if(len(a)<len(b)):
            a, b = b, a
        diferencia = len(a)-len(b)
        distancia += diferencia
        for i in b:
            if not (i in a):
                distancia += 1
        if (distancia == 1):
            return "IB"

    return "+1"

if __name__ == "__main__":    
    print(levenshtein("manisto","manito"))
    print(levenshtein("gatito","gato"))
    print(levenshtein("gallina","gallina"))
    print(levenshtein("sapa","sapo"))
           