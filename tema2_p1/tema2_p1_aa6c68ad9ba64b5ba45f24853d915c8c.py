# por favor escribe aquí tu función
def es_primo(c):
    if c<2:
       return False
       
    for num in range(2,c):
        if c%num==0:
           return False
           
    return True        