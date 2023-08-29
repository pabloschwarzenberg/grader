#Ordenar tres números
p=int(input())
n=int(input())
c=int(input())
if (p<=n<=c):
  print(p,",",n,",",c,)
if (c<=n<=p):
  print(c,",",n,",",p)
if (n<=c<=p):
  print(n,",",c,",",p)
if (c>=n>=p):
  print(p,",",n,",",c)