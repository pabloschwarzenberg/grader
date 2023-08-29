# por favor escribe aquí tu función
def es_primo(numero):
    x=2
    while x<numero:
        if numero%x!=0:
            return True
            x+=1
        elif numero%x==0:
            return False
    if numero==1:
        return False