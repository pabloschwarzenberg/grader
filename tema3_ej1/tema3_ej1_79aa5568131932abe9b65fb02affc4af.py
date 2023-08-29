def suma_divisores(a):
    n=1
    f=1
    while n<=a:
        if a%n==0:
            f=f+n
        n=n+1
    z=f-1-a
    if z==1:
      return z,True
    else:
      return z, False