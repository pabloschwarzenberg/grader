# completa el código de la función
def suma_divisores(a):
    lista=[]
    n=0
    for z in range(1,a):
        if a%z==0:
            n=n+z
            lista.append(z)
    if len(lista)==1:
        z=True
    else:
        z=False
    return n,z