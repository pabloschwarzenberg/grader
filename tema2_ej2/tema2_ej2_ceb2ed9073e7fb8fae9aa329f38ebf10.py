# completa el código de la función
def amigos(a,b):
    ab = a%b
    ba = b%a
    if ab == ba or a == 1 and b ==2:
        return False
    elif ab != ba:
        return True