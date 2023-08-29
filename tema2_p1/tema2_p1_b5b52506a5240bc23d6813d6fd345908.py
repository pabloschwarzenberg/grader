def es_primo(a):
    div = 0
    i = 1
    while i < a:
        if a%i == 0:
            div +=1
            i += 1
        else:
            i += 1
    if div == 1:
        return True
    else:
        return False