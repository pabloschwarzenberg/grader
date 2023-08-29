def es_primo(numero):
    a = 2
    b=0
    while a < numero:
        if numero%a==0:
            b=b+1
        a=a+1
    if b==0 and numero!=1:
        return True
    else:
        return False
