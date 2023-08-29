string = "estamos programando"
def jerigonzo(string):
    V = ["a","e","i","o","u"]
    o = []
    for i in string:
        o.append(i)
        if i in V:
            o.append("p")
            o.append(i)  
    u = "".join(o)
    return u
print(jerigonzo(string))         