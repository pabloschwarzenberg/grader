# por favor escribe aquí tu función
def es_primo(a):
    if(a>=2):
     for x in range(2, a):
       if (a%x==0):
        return False
       return True
    return False
    


