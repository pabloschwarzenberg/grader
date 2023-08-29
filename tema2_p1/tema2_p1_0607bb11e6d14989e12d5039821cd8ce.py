def es_primo(numero):
    d=2
    primo=True
    if numero==1:
        primo=False
    while d<numero:
     if numero%d==0:
        primo=False
        break
     d=d+1
    return (primo)
