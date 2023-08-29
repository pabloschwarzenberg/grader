def jerigonzo(string):
    lista=list(string)
    i=0
    while i<=len(lista)-2:
        if lista[i]=="a":
            lista.insert(i+1,"p")
            lista.insert(i+2,"a")
            i=i+3
        if lista[i]=="e":
            lista.insert(i+1,"p")
            lista.insert(i+2,"e")
            i=i+3
        if lista[i]=="i":
            lista.insert(i+1,"p")
            lista.insert(i+2,"i")
            i=i+3
        if lista[i]=="o":
            lista.insert(i+1,"p")
            lista.insert(i+2,"o")
            i=i+3
        if lista[i]=="u":
            lista.insert(i+1,"p")
            lista.insert(i+2,"u")
            i=i+3
        else:
            i=i+1
    if lista[len(lista)-1]=="a":
        lista.insert(len(lista),"p")
        lista.insert(len(lista)+1,"a")
    if lista[len(lista)-1]=="e":
        lista.insert(len(lista),"p")
        lista.insert(len(lista)+1,"e")
    if lista[len(lista)-1]=="i":
        lista.insert(len(lista),"p")
        lista.insert(len(lista)+1,"i")
    if lista[len(lista)-1]=="o":
        lista.insert(len(lista),"p")
        lista.insert(len(lista)+1,"o")
    if lista[len(lista)-1]=="u":
        lista.insert(len(lista),"p")
        lista.insert(len(lista)+1,"u")
        
    string="".join(lista)
    return string 

if __name__ == "__main__":
    pass
    a=input("ingrese una frase ")
    print(jerigonzo(a))