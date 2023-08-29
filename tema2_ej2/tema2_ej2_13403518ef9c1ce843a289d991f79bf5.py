# completa el código de la función
def amigos(a,b):
    adiv =[]
    bdiv =[]
    for i in range(2,a):
        if a%i ==0:
            adiv.append(i)
    for i in range(2,b):
        if b%i ==0:
          bdiv.append(i)
    if (sum(adiv)+1) ==b and (sum(bdiv)+1) ==a:
        return True
    else:
        return False
           