# por favor escribe aquí tu función
def es_primo(numero):
    if numero<2:
        return False
    i=2
    for i in range (2,int((numero)**(1/2)+1)):
        if (numero%i==0):
            return False
    else:
        return True  