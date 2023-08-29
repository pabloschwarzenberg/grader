def jerigonzo(n):
    T = []
    for P in n:
        for l in P:
            if l in "aeiouAEIOU":
                l = l + "p"+ l
            T.append(l)
    T = "".join(T)
    return T