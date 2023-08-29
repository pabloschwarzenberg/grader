#numeros amigos
def amigos(N,S):
  x=[]
  z=[]
  for i in range(1,N):
    if N%i==0:
      x.append(i)
  y=sum(x)
  for j in range(1,S):
    if S%j==0:
      z.append(j)
  g=sum(z)
  if g==N and y==S :
    return True  
  else:
    return False


           