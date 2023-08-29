def buscarTodas(a,b):
    largo=len(a)
    g = 0
    s=list(a)
    variables=""
    while g<largo :
        if s[g]==b:
            f=str(g)
            variables=variables +" "+ f
            g +=1
        else:
            g +=1
    h="".join(variables)
    h=h[1:]
    return  h

