# por favor escribe aquí tu función
def es_primo(numero):
    divisores=[0]
    for i in range(1, numero):
        if numero%i==0:
            divisores.append(i)
    x=sum(divisores)
    if x==1:
        return(True)
    else:
        return(False)
a=es_primo(7)
print(a)
           