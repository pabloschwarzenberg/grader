n=int(input())
n1=int(input())
n2=int(input())
if n<=n1:
    if n1<=n2 and n<=n2:
        print(n,",",n1,",",n2)
    elif n1>=n2 and n<=n2:
        print(n,",",n2,",",n1)
    elif n1>=n2 and n>=n2:
        print(n2,",",n,",",n1)
if n>n1:
    if n1<=n2 and n<=n2:
        print(n1,",",n,",",n2)
    elif n1>=n2:
        print(n2,",",n1,",",n)
    elif n1<=n2 and n>=n2:
        print(n1,",",n2,",",n)       
    
