def jerigonzo(string):
    string=list(string)
    indice=0
    while indice<len(string):
        letra=string[indice]
        if letra=="a" or letra=="A" or letra=="á" or letra=="Á":
            string.insert(indice+1,"pa")
        if letra=="e" or letra=="E" or letra=="é" or letra=="É":
            string.insert(indice+1,"pe")
        if letra=="i" or letra=="I" or letra=="í" or letra=="Í":
            string.insert(indice+1,"pi")
        if letra=="o" or letra=="O" or letra=="ó" or letra=="Ó":
            string.insert(indice+1,"po")
        if letra=="u" or letra=="U" or letra=="ú" or letra=="Ú":
            string.insert(indice+1,"pu")
        indice+=1
    frase="".join(string)
    return frase