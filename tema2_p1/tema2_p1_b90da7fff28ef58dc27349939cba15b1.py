# por favor escribe aquí tu función
def es_primo(numero):
    l=[2,3,5,7,11]
    for i in l:
        a=numero%i
        if numero==1:
            return False
        if numero==i:
            return True
        if a==0:
            return False
    return True