def jerigonzo(a):
    b=list("")
    for i in a:
        b.append(i)
        if i in ["a","e","i","o","u"]:
            b.append("p")
            b.append(i)
    palabra=""
    for i in b:
        palabra+=i
    return palabra