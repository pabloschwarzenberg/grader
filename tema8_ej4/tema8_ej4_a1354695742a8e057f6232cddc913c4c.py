def rot13(p):
    al="abcdefghijklmnopqrstuvwxyz"
    a=list(al)
    l=len(p)
    s=list(p)
    for i in range(l):
        d=s[i]
        n=a.index(d)
        if n<=12:
            s[i]= al[n+13]
        else :
            s[i]=al[n - 13]
    return (''.join(s))
           