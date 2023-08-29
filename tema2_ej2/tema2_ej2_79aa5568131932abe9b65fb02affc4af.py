def amigos(a,b):
    n=1
    f=1
    while n<=a:
        if a%n==0:
            f=f+n
        n=n+1
    z=f-1
    n2=1
    f2=1
    while n2<=b:
        if b%n2==0:
            f2=f2+n2
        n2=n2+1
    z2=f2-1
    if z==z2:
      return True
    else:
      return False

        
