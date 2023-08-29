def numero_perfecto(a):
    lista=[]
    d=2
    if a>1:
      lista.append(1)
    while d<a:
        if a%d==0:
            lista.append(d)
        d=d+1
    c=sum(lista)
    if (c==a):
        return True
    else:
        return False



           