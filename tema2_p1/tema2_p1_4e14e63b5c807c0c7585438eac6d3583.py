def es_primo(n):
    cantdiv=0
    for i in range(1,n+1):
        if n%i==0:
            cantdiv=cantdiv+1
    if cantdiv==2:
        return True
    else:
        return False