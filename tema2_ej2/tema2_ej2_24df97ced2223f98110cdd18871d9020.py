# completa el código de la función
def amigos(a,b):
   l1=[]
   l2=[]
   for i in range(1,a):
     if a%i==0:
       l1.append(i)
   y=sum(l1)
   for k in range(1,b):
     if b%k==0:
       l2.append(k)
   g=sum(l2)
   if g==a and y==b:
     return True
   else:
     return False
  
           