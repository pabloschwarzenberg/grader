# por favor escribe aquí tu función
a = 3
             
def es_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True
    
print(es_primo(a))
           