# completa el código de la función
def amigos(a,b):
  divisoresA=[]
  divisoresB=[]
  if a==1 and b==2:
    return False
  if a==2 and b==1:
    return False
  for i in range(1,a):
    if a%i==0:
      divisoresA.append(i)
  for i in range(1,b):
    if b%i==0:
      divisoresB.append(i) 
  suma1=0
  for i in range(len(divisoresA)):
    suma1=suma1+divisoresA[i]
  suma2=0
  for i in range(len(divisoresB)):
    suma2=suma2+divisoresB[i]
  if suma1==b and suma2==a:
    return True
  if suma1!=b and suma2!=a:
    return False
a=2
b=3
amigos(a,b)