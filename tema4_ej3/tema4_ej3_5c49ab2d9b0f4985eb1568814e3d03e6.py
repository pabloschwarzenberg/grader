def jerigonzo(string):
    lista=[]
    zero=0
    pucha="p"
    while zero<len(string):
        y=string[zero]
        if y=="a" or y=="e" or y=="i" or y=="o" or y=="u":
            lista.append(string[zero])
            lista.append(pucha)
            lista.append(string[zero])
        else:
            lista.append(string[zero])
        zero=zero+1
    string="".join(lista)
    return(string)
