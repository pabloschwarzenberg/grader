def levenshtein(palabraA,palabraB) :
    list_a = list(palabraA)
    list_b = list(palabraB)
    d=0
    x=0
    if palabraA==palabraB:
        d="0D"
    if len(palabraA)== len(palabraB) and palabraA != palabraB:
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                x = x+1
            else:
                x=x+0
        if x>1 :
            d="+1"
        else:
            d="1S"
    if len(palabraA)-len(palabraB)==1 or len(palabraB)-len(palabraA)==1 :
        if len(list_a)>len(list_b):
            list_b.append("X")
        else:
            list_a.append("X")
        for i in range(len(list_a)):
           if list_a[i]!=list_b[i]:
               x=x+1
           else:
               x=x+0
        if x>3:
            d="+1"
        else:
            d="IB"



    if (len(palabraA) - len(palabraB)) >= 2 or (len(palabraB) - len(palabraA)) >= 2:
        d="+1"

    return d
