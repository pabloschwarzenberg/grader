# por favor escribe aquí tu función
def es_primo(numero):
    numero=int(numero)
    if numero==1:
        return False
    if numero<2:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2,numero):
            if (numero%i)==0:
        #es divisible
                return False
            elif(i==numero-1):
                return True
           