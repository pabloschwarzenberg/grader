def jerigonzo(palabra):
    a=list(palabra)
    c=len(a)
    b=0
    while b < c:
        if a[b]=='a':
            a.insert(b+1,'p')
            a.insert(b+2,'a')
            c=c+2
            b+=3
        elif a[b]=='e':
            a.insert(b+1,'p')
            a.insert(b+2,'e')
            c=c+2
            b+=3 
        elif a[b]=='i':
            a.insert(b+1,'p')
            a.insert(b+2,'i')
            c=c+2
            b+=3
        elif a[b]=='o':
            a.insert(b+1,'p')
            a.insert(b+2,'o')
            c=c+2
            b+=3
        elif a[b]=='u':
            a.insert(b+1,'p')
            a.insert(b+2,'u')
            c=c+2*b
            b+=3
        else:
            b+=1
    z="".join(a)
    return z