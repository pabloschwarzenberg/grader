def jerigonzo(string):
    string=str(string)
    stringls=list(string)
    vocales=["a","e","i","o","u"]
    n=1
    for i in stringls:        
        if vocales.count(i)>=1:
            e="p"+i
            stringls.insert(n,e)
            n+=1
            continue
        else:
            n+=1
            continue
    string="".join(stringls)
    return string