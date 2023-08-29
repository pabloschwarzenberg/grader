# por favor escribe aquí tu función
def es_primo(numero):
    i=0
    div=2
    while i<=numero:
        if div!=numero and numero%div==0:
            return False
        elif numero!=1:
            return True
        else:
            return False
    div=div+1
