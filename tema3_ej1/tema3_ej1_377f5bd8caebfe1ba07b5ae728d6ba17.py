# completa el código de la función
def suma_divisores(a):
    division=1
    guardo=0
    while division!=a:
        if (a%division==0):
            guardo=guardo+division
            division=division+1
        else:  
          division=division+1
    if guardo==1:
        return guardo , True
    else:
        return guardo , False
