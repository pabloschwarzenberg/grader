# por favor escribe aquí tu función
def es_primo(num):
    fl=1
    if num>2:
        for W in range(2,num):
            if (num % W==0):
                fl=0
                break
    else:
        if num==2:
            fl=1
        else:
            fl=0
    if fl==0:
        return False
    else:
        return True