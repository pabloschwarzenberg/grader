def levenshtein(palabra1,palabra2):
    if len(palabra1) == len(palabra2):
        dist = 0
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]: dist += 1
        if dist > 1:
            return "+1"
        elif dist == 1:
            return "1S"
        elif dist == 0:
            return "0D"
    elif abs(len(palabra1) - len(palabra2)) == 1:
        for j in range(min(len(palabra1), len(palabra2))):
            if palabra1[j] != palabra2[j]:
                return "+1"
        return "IB"
    else:
        return "+1"
   
if __name__=="__main__":
    pass
           