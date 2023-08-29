# completa el código de la función
def divisores(numero):
    divi=[]
    for i in range(1,numero):
        if numero%i==0:
            divi.append(i)
    return divi


def amigos(a,b):
    x=divisores(a)
    y=divisores(b)
    print(x,y)
    valor=False
    if sum(x)==b and sum(y)==a:
        valor=True

    return valor


           