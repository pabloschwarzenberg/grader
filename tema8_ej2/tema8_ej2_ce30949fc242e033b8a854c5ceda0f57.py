def buscarTodas(a,b):
    c=0
    x=''
    for i in a:
        if b==i:
            x+=str(c)+' '
        c+=1
    x=x.strip( )
    return x