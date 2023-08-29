# por favor escribe aquí tu función
def es_primo(numero):
    c=0
    for i in range(1,numero+1):
        if numero%i==0:
            c+=1
    if c>2 or numero==1:
        primo=False
    else:
        primo=True
    return primo
