# por favor escribe aquí tu función
def es_primo(numero):
    c=0
    for x in range (2, numero+1):
        if numero%x==0:
            c+=x
    if c==numero:
        return True 
    else:
        return False
  
           