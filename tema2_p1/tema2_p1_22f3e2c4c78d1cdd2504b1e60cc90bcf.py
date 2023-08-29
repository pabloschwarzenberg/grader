# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
      return False
    es_primo= True
    
    for d in range (2,numero):
        if numero%d ==0:
            es_primo=False
            break
    if es_primo:
        return True
    else:
        return False

           