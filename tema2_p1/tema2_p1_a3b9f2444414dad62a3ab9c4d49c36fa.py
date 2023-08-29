# por favor escribe aquí tu función
def es_primo(numero):
    x=0
    i=1
    while i<=numero:
        if numero%i==0:

            x=x+1

        i=i+1

    if x==2:
        return True
    else:
        return False