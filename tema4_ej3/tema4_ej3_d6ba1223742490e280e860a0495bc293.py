def jerigonzo(string):
    #funcion basestring
    strAux =""
    ind = 0
    largo = len(string)
    listavocales=["a","e","i","o","u"]
    for i in string:
     if(i in listavocales):
        try:
            ca="p"
            strAux += string[ind]
            strAux += string[ind +1].replace(string[ind + 1], ca)
            if(largo != (ind + 1)):
                ind += 1
        except:
            if(i in listavocales):
                return strAux + "p"
            return strAux
     else:
        strAux += i
        ind += 1
    return strAux
