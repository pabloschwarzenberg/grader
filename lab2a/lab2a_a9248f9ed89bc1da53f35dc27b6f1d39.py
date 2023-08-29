#múltiplos
i=int(input('numero de inicio :'))
f=int(input('numero de fin :'))
while i<=f:
    mu1=i%2
    mu2=i%7
    if mu1==0 and mu2==0:
        print(i)
    i=i+1    
        
        