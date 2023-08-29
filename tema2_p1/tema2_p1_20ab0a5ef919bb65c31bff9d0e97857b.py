# por favor escribe aquí tu función
def es_primo(numero):
    c=1
    p=0
    while(c<=numero):
       
        if(numero%c==0):
            p=p+1
        c=c+1
        if(p>2):
            break
    
    if(p==2):
        return True
    else:
        return False

           