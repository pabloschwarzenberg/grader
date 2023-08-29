def jerigonzo(a):
    traducido=""
    v="a","e","i","o","u"
    for i in a:
        if i in v:
            traducido = traducido + i
            traducido = traducido + "p"
            traducido = traducido + i
        else:
            traducido= traducido + i
    return traducido
         