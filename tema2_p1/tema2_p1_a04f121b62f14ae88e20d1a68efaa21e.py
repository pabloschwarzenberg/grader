def es_primo(numero):
    num=2
    if numero<=1:
        return False
    elif numero==2:
        return True
    while num<numero:
        if numero%num==0:
            return False
        num=num+1
        return True