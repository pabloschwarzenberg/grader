def suma_divisores(n):
    divisores=[1]
    for i in range(2,n-1):
        if n%i==0:
            divisores.append(i)
  
    if n==1:
        return n-1,False
        
        
    if len(divisores)==1:
        return (len(divisores), True)
    if len(divisores)!=1 :
        return n-1,False