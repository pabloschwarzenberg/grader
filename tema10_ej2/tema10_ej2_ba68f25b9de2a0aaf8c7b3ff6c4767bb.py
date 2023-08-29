from Levenshtein import distance

def levenshtein(s1, s2):
    d = distance(s1, s2)
    if d == 0:
        return "0D"
    elif d == 1:
        if len(s1) > len(s2):
            return "IB"
        else:
            return "IS"
    else:
        return "+1"
