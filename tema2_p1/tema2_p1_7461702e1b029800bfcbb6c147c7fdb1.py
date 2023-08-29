def es_primo(numero):
    i=1
    c=0
    while i<=numero:
        if numero%i==0:
            c=c+1
        i=i+1
    if c>2 or numero==1:
        return False
    else:
        return True
         