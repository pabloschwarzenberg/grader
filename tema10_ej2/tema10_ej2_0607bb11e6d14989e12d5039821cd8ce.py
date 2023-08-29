def levenshtein(palabra1,palabra2):
    cuenta=0
    if len(palabra1)==len(palabra2):
       for p in range(len(palabra1)):
           if palabra1[p]!=palabra2[p]:
               cuenta=cuenta+1
       if cuenta==0:
           return "0D"
       if cuenta==1:
           return "1S"
       else:
           return "+1"
    elif len(palabra1)+1==len(palabra2) or len(palabra1)==len(palabra2)+1:
       if len(palabra2)>len(palabra1):
        for p in palabra1:
            if palabra2.find(p)==-1:
                return "+1"
                break
       if len(palabra1)>len(palabra2):
        for p in palabra2:
            if palabra1.find(p)==-1:
                return "+1"
                break
       return "IB"
    else:
        return "+1"
           