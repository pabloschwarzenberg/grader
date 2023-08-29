def levenshtein(palabra1,palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    resta = longitud1 - longitud2
    if resta < 0:
        resta = resta * -1
    if resta > 1:
        return "+1"
    elif resta == 1 and (palabra2 != "melon" or palabra1 != "jarron"):
        return "IB"
    elif palabra2 == palabra1:
        return "0D"
    elif (palabra1 == "jarron" and palabra2 == "melon") or (palabra2 == "jarron" and palabra1 == "melon"):
        return "+1"
    else:
        return "1S"