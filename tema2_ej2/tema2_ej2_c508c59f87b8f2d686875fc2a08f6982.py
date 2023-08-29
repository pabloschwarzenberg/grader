def amigos(a,b):
    i=1
    suma1=0
    n=1
    suma2=0
    while i<=a:
         c=a%i
         if c==0:
            suma1=suma1+i
         i+=1
    while n<=b:
         d=b%n
         if d==0:
            suma2=suma2+n
         n+=1
    if suma1==suma2 and a!=b:
         return True
    else:
         return False
