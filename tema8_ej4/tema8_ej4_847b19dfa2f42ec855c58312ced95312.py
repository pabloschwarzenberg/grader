def cambiar_letra(letra):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    po=abc.index(letra)
    if 0<=po<13:
        return (abc[po+13])
    if 12<po<26:
        return (abc[po-13])
def rot13(palabra):
    listap=list(palabra)
    n=0
    while n<len(listap):
        listap[n]=cambiar_letra(listap[n])
        n+=1
    pf="".join(listap)
    return pf