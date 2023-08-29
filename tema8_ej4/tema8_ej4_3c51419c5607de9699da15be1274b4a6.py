def string_lista(strs):
    lista = []
    for i in strs:
        lista.append(i)
    return lista
def lista_string(lista):
    strs = "".join(lista)
    return strs
def rot13(txt):
    list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    list2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    txt = string_lista(txt)
    num = []
    for i in txt:
        list1 = lista_string(list1)
        a = list1.find(i)
        if a == -1:
            a = list2.index(i)
            b = list1[a]
            num.append(b)
        elif a != -1:
            b = list2[a]
            num.append(b)
        list1 = string_lista(list1)
    num = lista_string(num)
    return num
if __name__=="__main__":
    a = str(input("Ingresa la palabra que quieres encriptar o desencriptar."))
    a = a.lower()

   