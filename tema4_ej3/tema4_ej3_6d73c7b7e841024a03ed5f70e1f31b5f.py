def jerigonzo(string):
    vocales=("a","e","i","o","u")
    palabra=[]
    for i in range(0,len(string)):
        if string[i] in vocales: 
            palabra.append(string[i]+"p"+string[i])
        else: palabra.append(string[i])
    string="".join(palabra)   
    return string
         