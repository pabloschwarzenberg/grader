def jerigonzo(string):
    conver = []
    for P in string:
        for L in P:
            if L in "aeiouAEIOU":
                L = L + "p"+ L
            conver.append(L)
    conver = "".join(conver)
    return conver
         