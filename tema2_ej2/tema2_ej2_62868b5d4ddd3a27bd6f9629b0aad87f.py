# completa el código de la función
def amigos(a,b):
    h=0
    k=0
    diva=a
    divb=b
    while diva>0:
        restoa=a%diva
        if restoa==0:
            h+=diva
        diva-=1
    while divb>0:
        restob=b%divb
        if restob==0:
            k+=divb
        divb-=1
    if k==h and a!=b:
        return True
    else:
        return False

