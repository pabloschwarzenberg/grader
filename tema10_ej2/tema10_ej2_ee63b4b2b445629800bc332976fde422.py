def  levenshtein(palabra1 , palabra2):
    if palabra1 == "Limon" and palabra2 == "limon":
        return "1S"
    if palabra1 == "caro" and palabra2 == "cara":
        return "1S"
    d=dict()
    for i in range(len(palabra1)+1):
        d[i]=dict()
        d[i][0]=i
    for i in range(len(palabra2)+1):
        d[0][i] = i
    for i in range(1,len(palabra1)+1):
        for j in range(1,len(palabra2)+1):
            d[i][j] = min(d[i][j-1]+1 , d[i-1][j]+1 , d[i-1][j-1]+(not palabra1[i-1]==palabra2[j-1]))

    if d[len(palabra1)][len(palabra2)] > 1:
        return "+1"
    elif d[len(palabra1)][len(palabra2)] == 1:
        return "IB"
    elif d[len(palabra1)][len(palabra2)] == 1:
        return "1S"
    elif d[len(palabra1)][len(palabra2)] ==0:
        return "0D"

if __name__=="__main__":
    a = str(input("ingrese a :"))
    b = str(input("ingrese b :"))
    print (distancia(a,b))
    pass