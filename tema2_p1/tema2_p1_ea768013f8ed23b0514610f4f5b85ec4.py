# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
        return False
    if numero==2 or numero==3:
        return True
    elif numero%2==0 or numero%3==0:
        return False
    else:
        return True 
