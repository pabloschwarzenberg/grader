# por favor escribe aquí tu función
def es_primo(numero):
    i=2
    valor=0
    while i<numero:
        if numero%i==0:
            valor=1
        i=i+1    
    if valor==1:
        valor=False
    elif numero==1:
        valor=False
    else:
        valor=True
    return valor
numero=3
es_primo(numero)
print(es_primo(numero))           