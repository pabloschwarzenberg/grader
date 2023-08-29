# por favor escribe aquí tu función
def es_primo(numero):
    primo = True
    i = 2
    if numero == 1:
        primo = False
    else:
        while i < (numero-1):
            if numero%i == 0:
                primo = False
            i = i+1
    
        
    
    return primo
           