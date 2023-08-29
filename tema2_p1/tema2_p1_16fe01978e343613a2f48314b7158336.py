# por favor escribe aquí tu función
def es_primo(numero):
    i = 2
    primo = True
    while i<numero:
        if numero%i == 0:
           primo = False
           break
        i = i + 1
    if primo and numero>1:
           return True
    else:
           return False
           