def jerigonzo(palabra) :
    list_palabra=list(palabra)
    palabra_jeri=[]
    for i in list_palabra :
        if i== "a" or i=="e" or i=="i" or i== "o" or i=="u" :
            palabra_jeri.append(i)
            palabra_jeri.append("p")
            palabra_jeri.append(i)
        else:
            palabra_jeri.append(i)

    palabra_final="".join(palabra_jeri)

    return palabra_final