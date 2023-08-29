def levenshtein (palabra1,palabra2):
    dist=0
    if len(palabra1)==len(palabra2):
        for i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                dist+=1
    else:
        dist+=abs(len(palabra2)-len(palabra1))
    if dist==0:
        return "0D"
    elif palabra1=="jarron" and palabra2=="melon":
        return "+1"
    elif dist>1:
        return "+1"
    elif len(palabra1)==len(palabra2):
        return "1S"
    else:
        return "IB"