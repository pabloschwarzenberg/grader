# completa el código de la función
def amigos(a,b):
    ba = 0
    bb = 0
    i = 1
    j = 1
    while i < a:
        if a%i == 0:
            ba = ba+i
        i = i+1
    while j < b:
        if b%j == 0:
            bb = bb+j
        j = j+1
    if a == bb and b == ba:
        return True
    else:
        return False
           