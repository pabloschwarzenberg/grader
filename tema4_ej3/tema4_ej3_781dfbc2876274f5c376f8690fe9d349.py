def jerigonzo(string):
    strlist=list(string)
    vocales=["a", "e", "i", "o", "u"]
    indic=0
    for i in string:
        if (i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u"):
            indice=(strlist.index(i, indic))+1
            indic=indice+1
            strlist.insert(indice, str("p"+i))
    string="".join(strlist)
    return string

if __name__ == "__main__":
    string=str(input("ingresa una palabra: "))
    print(jerigonzo(string))
         