def levenshtein(palabra1,palabra2):
    if len(palabra1)>len(palabra2):
        l1=list(palabra1)
        l2=list(palabra2)
    else:
        l1=list(palabra2)
        l2=list(palabra1)
    d=abs(len(l1)-len(l2))
    if d>1:
        return "+1"
    elif d==1:
        diferencias=0
        for i in range(len(l2)):
            if l2[i] not in l1:
                diferencias+=1
        diferencias+=1
        if diferencias==1:
            return "IB"
        else:
            return "+1"
    else:
        diferencias=0
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                diferencias+=1
        if diferencias>1:
            return "+1"
        elif diferencias==0:
            return "0D"
        else:
            return "1S"

if __name__ == "__main__":
    print(levenshtein("gato","gatito"))
    print(levenshtein("hola","ola"))
    print(levenshtein("gallina","gallina"))
    print(levenshtein("caro","cara"))
    print(levenshtein("jaron","jarron"))
    print(levenshtein("Limon","limon"))
    print(levenshtein("jarron","melon"))