def amigos(N,S):
  a=[]
  b=[]
  for i in range(1,N):
    if N%i==0:
      a.append(i)
  abc=sum(a)
  for j in range(1,S):
    if S%j==0:
      b.append(j)
  ab=sum(b)
  if ab==N and abc==S :
    return True  
  else:
    return False
      