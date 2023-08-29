#Hito 1 Amigos
def amigos(a,b):
    ra=range(1,a)
    rb=range(1,b)
    fa=0
    for i in ra:
        if (a%i)==0:
            fa=fa+i

    fb=0
    for x in rb:
        if (b%x)==0:
            fb=fb+x
        
    if a==1 and b==2 or b==1 and a==2:
        return False
    elif fa==b or fb==a:
        return True
    else:
        return False

