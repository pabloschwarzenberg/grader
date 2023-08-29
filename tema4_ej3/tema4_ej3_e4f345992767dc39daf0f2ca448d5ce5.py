def jerigonzo(string):
    c = []
    for p in string:
        for l in p:
            if l in "aeiouAEIOU":
                l = l + "p"+ l
            c.append(l)
    c = "".join(c)
    return c