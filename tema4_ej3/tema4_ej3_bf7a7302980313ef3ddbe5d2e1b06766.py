#Jerigonzo
def jerigonzo(string):
    pal=list(string.lower())
    pal_aux=[]
    for i in range(len(string)):
        if(pal[i]=="a" or pal[i]=="e" or pal[i]=="i" or pal[i]=="o" or pal[i]=="u"):
            pal_aux.append(pal[i])
            pal_aux.append("p")
            pal_aux.append(pal[i])
        else:    
            pal_aux.append(pal[i])
    return ("".join(pal_aux))