# por favor escribe aquí tu función
def es_primo(numero):
    contando=0
    for l in range(1,numero+1):
        if numero%l==0:
           contando+=1
    if contando==2:
        return True
    else:
        return False