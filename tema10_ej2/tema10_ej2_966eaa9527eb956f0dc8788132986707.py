def levenshtein(p1,p2):
    operacion = 0
    if len(p1) == len(p2):
        for i in range (0,len(p1)):
            if p1[i] !=  p2[i]:
                operacion += 1
        if operacion == 1:
            return '1S'
    elif len(p1) != len(p2):
        operacion += abs(len(p1)-len(p2))
        for i in p1:
            if i not in p2:
                operacion += 1
        if operacion == 1:
            return 'IB'
    if operacion > 1:
        return '+1'
    elif operacion == 0:
        return '0D'
if __name__=="__main__":
    pass
           