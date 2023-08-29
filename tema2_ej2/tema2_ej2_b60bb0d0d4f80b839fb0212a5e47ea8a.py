# completa el código de la función
def amigos(a,b):
  return
def amigos(A,B):
    S=int(0)
    k=int(1)
    z=int(0)
    n=int(1)
   

    while k<A:
        if (A%k)==0:
            S=S+k
            k=k+1
            
        else:
            k=k+1
    while n<B:
        if (B%n)==0:
            z=z+n
            n=n+1
            
        else:
            n=n+1
            
    if z==A and S==B:
        return True
    else:
        return False
   
           