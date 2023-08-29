def jerigonzo(str):
    lista=[]
    finale = []
    lista.extend(str)
    xsumator=""
    for rec in lista:
        if rec == "a" or rec == "e" or rec == "i" or rec == "o" or rec == "u":
            letra = rec
            rec = rec + "p" + rec
            finale.append(rec)
        else:
            finale.append(rec)
    for i in range(0, len(finale)):
        xsumator += finale[i]
    return xsumator