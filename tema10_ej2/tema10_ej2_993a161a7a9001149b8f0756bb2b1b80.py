def levenshtein(palabra1,palabra2):
    a=len(palabra1)
    b=len(palabra2)
    c=a-b
    if c<-1 or c>=1:
        return "+1"
    if c==1 or c==-1:
        return "IB"

    if c==0:
        if palabra1==palabra2:
            return "0D"
        else:
            return "1S"

           