def jerigonzo(string):
    jerigonzoo=[]
    vocales=("a","e","i","o","u")
    for i in string:
        if i in vocales:
            i=i+"p"+ i
        jerigonzoo.append(i)
    string="".join(jerigonzoo)
    return string
         