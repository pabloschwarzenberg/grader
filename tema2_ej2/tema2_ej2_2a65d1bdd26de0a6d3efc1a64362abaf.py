# completa el código de la función
def amigos(a,b):
    amigo1 = 1
    amigo2 = 1
    for i in range (2,a):
        if(a%i == 0):
            amigo1= amigo1+i
    for i in range (2,b):
        if(b%i == 0):
            amigo2 = amigo2+i
    if(amigo1 == b and amigo2 == a):
        return True
    else:
        return False
           