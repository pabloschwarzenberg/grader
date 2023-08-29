def jerigonzo(string):
    string=string.lower()
    lista=list(string)
    vocales=["a","e","i","o","u"]
    large=lista.count("a")+lista.count("e")+lista.count("i")+lista.count("o")+lista.count("u")
    for i in range(0,len(lista)+large-1):
        if lista[i] in vocales:
            lista.insert(i+1,"p"+lista[i])
    string="".join(lista)
    return(string)

if __name__ == "__main__":
    print("Este programa transforma palabras a jerigonzo.")
    palabra=input("Ingrese palabra a transformar: ")
    asd=jerigonzo(palabra)
    print(palabra.capitalize(),"en jerigonzo es",asd.capitalize())
         