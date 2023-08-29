def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    else:
        if len(palabra1)==len(palabra2):
            c=0
            for i in range(len(palabra1)):
                if palabra1[i]!=palabra2[i]:
                    c+=1
            if c==1:
                return "1S"
        else:
            x=list(palabra2)
            for i in range(len(palabra1)):
                if palabra1[i] in x:
                    x.remove(palabra1[i])
            if abs(len(palabra1)-len(palabra2))==len(x):
                if len(x)==1:
                    return "IB"
                else:
                    return "+1"
            else:
                return "+1"


if __name__=="__main__":

    levenshtein("jarron", "melon")