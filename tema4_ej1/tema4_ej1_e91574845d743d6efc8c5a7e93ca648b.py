import random
def ocultar_letras(palabra,cantidad):
    lst=list(palabra)
    i=0
    while i < cantidad:
        u=random.randint(0,len(palabra)-1)
        del lst[u]
        lst.insert(u,"_")
        i=i+1
    palabra=("".join(lst))
    return(palabra)

def revisar_letra(palabra_secreta,palabra,letra):
    i=1
    lct=list(palabra_secreta)
    lst=list(palabra)
    while i < lct.count(letra):
        u=lct.index(letra)
        del lst[u]
        lst.insert(u,letra)
        i=i+1
    palabra=("".join(lst))
    return(palabra)

if __name__ == "__main__":
    pass
         