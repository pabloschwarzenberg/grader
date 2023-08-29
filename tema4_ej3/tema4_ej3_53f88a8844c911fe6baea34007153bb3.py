def jerigonzo(string):
    lista_string=list(string)
    for i in range(0,len(lista_string)):
        if lista_string[i]=="A" or lista_string[i]=="a" or lista_string[i]=="E" or lista_string[i]=="e":
            lista_string[i]=lista_string[i] + "p" + lista_string[i]
        elif lista_string[i]=="I" or lista_string[i]=="i" or lista_string[i]=="O" or lista_string[i]=="o" or lista_string[i]=="U" or lista_string[i]=="u":
            lista_string[i]=lista_string[i] +"p" + lista_string[i]

    return "".join(lista_string)

if __name__=="__main__":
    string=input("Ingrese una palabra para traducir: ")
    print(jerigonzo(string))
         