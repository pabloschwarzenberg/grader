def es_primo(numero):
    if numero==1:
        return False
    else:
        for h in range(2,numero):
            if(numero%h)==0:
                return False
        return True
        
           