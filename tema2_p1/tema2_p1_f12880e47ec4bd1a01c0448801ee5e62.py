#Daniel Barrios
def es_primo(numero):
    cont=0
    for i in range(1,numero+1):
        if numero%i==0:
            cont=cont+1
    if cont==2:
        return True
    else:
        return False