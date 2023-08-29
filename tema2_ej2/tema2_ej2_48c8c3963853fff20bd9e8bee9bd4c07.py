# completa el código de la función
import sys
def amigos(a,b):
  i=1
  u=0
  p=0
  q=0
  t=0
  divisores1=[]
  divisores2=[]
  if (a==1 or a==2) and (b==1 or b==2):
    return False
    sys.exit()
  else:
    while (i<a or i<b) and(i!=a or i!=b):
      n1=a%i
      n2=b%i
      if n1==0 and i!=a:
        divisores1.append(i)
      if n2==0 and i!=b:
        divisores2.append(i)
      i=i+1
    n1=len(divisores1)
    n2=len(divisores2)
    while u<n1:
      p=divisores1[u]+p
      u=u+1
    while t<n2:
      q=divisores2[t]+q
      t=t+1
    if p==b or q==a:
      return True
    else:
      return False