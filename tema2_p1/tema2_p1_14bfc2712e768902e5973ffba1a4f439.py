def es_primo(numero):
    a=0
    for f in range(numero):
        if numero%(f+1)==0:
            a+=1
    if a ==2:
        return True
    else:
        return False
           