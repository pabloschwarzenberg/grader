# por favor escribe aquí tu función
def es_primo(y):
    if y<2:
       return False

    for num in range(2,y):
        if y%num==0:
           return False

    return True