def amigos(a,b):
    d=a
    e=b
    h=0
    c=0
    j=0
    while a>1:
        a=a-1
        if d%a==0:
            h=h+a
            if h==b:
                c=1
    while b>1:
         b=b-1
         if e%b==0:
             j=j+b
             if j==d:
                 c=c+1
    if c==2:
        return True
    else:
        return False