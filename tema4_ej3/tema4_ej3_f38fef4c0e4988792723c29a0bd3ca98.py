diccionario={"a":"apa","e":"epe","i":"ipi","o":"opo","u":"upu"}


def jerigonzo(string):
    string_l=list(string)
    i=0
    lista=[]
    while i<len(string_l):
        if string_l[i]=="a" or string_l[i]=="a" or string_l[i]=="e" or string_l[i]=="i" or string_l[i]=="o" or string_l[i]=="u":
            if string_l[i]=="a":
                d=diccionario["a"]
                lista.append(d)
            elif string_l[i]=="e":
                d=diccionario["e"]
                lista.append(d)
            elif string_l[i]=="o":
                d=diccionario["o"]
                lista.append(d)
            elif string_l[i]=="i":
                d=diccionario["i"]
                lista.append(d)
            elif string_l[i]=="u":
                d=diccionario["u"]
                lista.append(d)
            i=i+1
        else:
            lista.append(string_l[i])
            i=i+1
    frage="".join(lista)
    return frage

if __name__ == "__main__":
    string=str(input("Ingrese una palabra para traducirla a jerigonzo: "))
    frase=jerigonzo(string)
    print(frase)

         