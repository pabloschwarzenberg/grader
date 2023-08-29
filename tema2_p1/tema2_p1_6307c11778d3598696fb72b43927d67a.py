# por favor escribe aquí tu función
#def es_primo(numero):

 #return
def es_primo(numero):
    if numero==1:
        return False
    es_primo = True
    for i in range(2,numero):
        if numero%i == 0:
            es_primo = False
    return es_primo

           