# completa el código de la función
def amigos(a,b):
    primerN=(a,b)[0]
    segundoN=(a,b)[1]
    x=1
    evaluacion=0
    while x<primerN:
        if primerN%x==0:
            evaluacion+=x
        x+=1
    if evaluacion==segundoN:
        return True
    else:
        return False