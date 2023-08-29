def es_primo(num):
    p = True
    if num == 2 or num == 3:
        p = True
    elif num == 1:
        p = False
    elif num%2 == 0:
        p = False
    elif num%3 == 0:
        p = False


    return p