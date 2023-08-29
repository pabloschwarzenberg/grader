# completa el código de la función
def amigos(a,b):
    sa=0
    sb=0
    for i in range(a-1):
        if(a%(i+1)==0):
            sa+=(i+1)
    for i in range(b-1):
        if(b%(i+1)==0):
            sb+=(i+1)
    if((sa==b)and(sb==a)):
        return True
    else:
        return False