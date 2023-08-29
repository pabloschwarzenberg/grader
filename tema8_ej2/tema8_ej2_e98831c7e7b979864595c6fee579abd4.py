def buscarTodas(a,b):
    i=0
    c=""
    for i in range(len(a)):
       if a[i]==b:
           c=c+" "+str(i)
    i+=1
    c=c.strip()
    return c