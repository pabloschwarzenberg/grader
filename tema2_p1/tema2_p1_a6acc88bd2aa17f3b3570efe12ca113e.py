def es_primo(numero):
    o=0
    for x in range(1,numero+1):
        if numero%x==0:
            o+=x
    if o==numero+1:
        return True
    else:
        return False