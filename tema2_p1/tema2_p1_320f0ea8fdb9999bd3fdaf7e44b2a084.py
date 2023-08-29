def es_primo(numero):
    a=2
    if numero==1:
        return False
    while a<=numero//2:
        if numero%a==0:
            return False
        a+=1
    return True