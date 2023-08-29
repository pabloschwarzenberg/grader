def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)==len(palabra2):
        reemplazar=0
        for i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                reemplazar+=1
        if reemplazar>1:
            return "+1"
        else:
            return "1S"
    elif abs(len(palabra1)-len(palabra2))==1:
        if len(palabra1)>len(palabra2):
            for j in range(len(palabra1)):
                if palabra1[:j]+palabra1[j+1:]==palabra2:
                    return "IB"
            return "+1"
        else:
            for k in range(len(palabra2)):
                if palabra2[:k]+palabra2[k+1:]==palabra1:
                    return "IB"
            return "+1"
    else:
        return "+1"
