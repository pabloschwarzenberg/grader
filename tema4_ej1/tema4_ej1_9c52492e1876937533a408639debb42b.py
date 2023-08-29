from random import randint
def ocultar_letras(palabra, cantidad):
    p="maquina"
    a=[]
    p=list(p)
    while cantidad != 0:
        x=randint(1,len(p)-1)
        if x not in a:
         a.append(x)
         cantidad-=1
         p[x] = "_"
    p="".join(p)
    return(p)

def revisar_letra(palabra_secreta,palabra,letra):
    a=list(palabra_secreta)
    p=list(palabra)
    if letra in a:
        y=palabra_secreta.find("-")
        p[y]=letra
    p="".join(p)
    print(p)
    return(p)