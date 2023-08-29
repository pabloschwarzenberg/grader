# completa el código de la función
def amigos(a,b):
    sa=0
    sb=0
    for da in range(1,a):
        if a%da==0:
            sa=sa+da
    for db in range(2,b):
        if b%db==0:
            sb=sb+db
    if sa==b or sb==a:
        return True
    else:
        return False


           