def suma_divisores(a):
    n=1
    k=[]
    while n<a:
        if a%n==0:
            k.append(n)
        n=n+1
    x=0
    s=0
    while x<len(k):
        s=s+k[x]
        x=x+1
    if s==1:
        return s, True
    else:
        return s, False