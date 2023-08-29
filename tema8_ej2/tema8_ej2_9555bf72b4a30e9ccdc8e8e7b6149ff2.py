def buscarTodas(a,b):
    c=""
    for i in range(len(a)):
        if a[i]==b:
            c+=str(i)+" "
    return c[0:-1]
       