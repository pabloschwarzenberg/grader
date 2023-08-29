def buscarTodas(a,b):
    if b in a:
        string=""
        i=0
        while i < len(a):
            if a[i]==b:
                pos=i
                string=string+" "+str(i)
            i+=1
        string=string.strip()
    return string
           