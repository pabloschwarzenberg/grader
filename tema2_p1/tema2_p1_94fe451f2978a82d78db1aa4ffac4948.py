# por favor escribe aquí tu función
def es_primo(x):
    c = 0
    for i in range(1, x+1):
        if x%i==0:
            c = c+1
    
    if c==2:
        return(True)
    else:
        return(False)
           