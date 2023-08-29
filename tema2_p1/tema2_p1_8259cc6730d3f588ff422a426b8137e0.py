# por favor escribe aquí tu función
def es_primo(numero):
    al=[]
    c=1
    while c<=numero:
        if numero%c==0:
            al.append(c)
            c=c+1
        else:
            c=c+1
    if sum(al)==numero+1:
        return True
    else:
        return False
           