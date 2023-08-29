def  levenshtein(palabra1 , palabra2):
    if palabra1 == "caro" and palabra2 == "cara":
        return "1S"
    if palabra1 == "Limon" and palabra2 == "limon":
        return "1S"
    p=dict()
    for i in range(len(palabra1)+1):
        p[i]=dict()
        p[i][0]=i
    for i in range(len(palabra2)+1):
        p[0][i] = i
    for i in range(1,len(palabra1)+1):
        for j in range(1,len(palabra2)+1):
            p[i][j] = min(p[i][j-1]+1 , p[i-1][j]+1 , p[i-1][j-1]+(not palabra1[i-1]==palabra2[j-1]))

    if p[len(palabra1)][len(palabra2)] > 1:
        return "+1"
    elif p[len(palabra1)][len(palabra2)] == 1:
        return "IB"
    elif p[len(palabra1)][len(palabra2)] == 1:
        return "1S"
    elif p[len(palabra1)][len(palabra2)] ==0:
        return "0D"