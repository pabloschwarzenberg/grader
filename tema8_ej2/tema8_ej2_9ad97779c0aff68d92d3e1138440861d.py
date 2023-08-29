def buscarTodas(a,b):
    i=0
    m=""

    while i<len(a):
        if a[i]==b:
            m=m+str(i) +" "
        i=i+1
    return m.strip()
    
           