# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 2:
       return True
    if numero>1 and numero%1==0 and numero%numero==0 and not(numero%2==0):
       return True
    else:
       return False
    
       
           