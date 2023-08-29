def levenshtein(p1,p2):
    diferencia = 0
    igualT = True
    p1 = list(p1)
    p2 = list(p2)

    if len(p1) != len(p2):
        igualT = False
        if len(p1) > len(p2):
            while len(p1) > len(p2):
                p2.append("")
        else:
            while len(p2) > len(p1):
                p1.append("")
 
    if "" in p1 or "" in p2 and len(p1) == len(p2):
        igualT = False
        i = 0
        while i < len(p1):
            if p1[i] == "" or p2[i] == "":
                diferencia += 1
                i += 1
            elif  p1[i] != p2[i]:
                diferencia += 1
                i +=1
            else:
                i += 1
    if "" not in p1 and "" not in p2 and len(p1) == len(p2):
        i = 0
        while i < len(p1):
            if p1[i] != p2[i]:
                diferencia += 1
                i += 1
            else:
                i += 1
            
    if diferencia > 1:
        return "+1"
    if diferencia == 1 and not igualT:
        return "IB"
    if diferencia == 1 and igualT:
        return "1S"
    if diferencia == 0 and igualT:
        return "0D"