def amigos(A,x):
  divisoresA=[]
  divisoresB=[]
  if A==1 and x==2:
    return False
  if A==2 and x==1:
    return False
  for i in range(1,A):
    if A%i==0:
      divisoresA.append(i)
  for i in range(1,x):
    if x%i==0:
      divisoresB.append(i) 
  suma1=0
  for i in range(len(divisoresA)):
    suma1=suma1+divisoresA[i]
  suma2=0
  for i in range(len(divisoresB)):
    suma2=suma2+divisoresB[i]
  if suma1==x and suma2==A:
    return True
  if suma1!=x and suma2!=A:
    return False
A=2
x=3
amigos(A,x)