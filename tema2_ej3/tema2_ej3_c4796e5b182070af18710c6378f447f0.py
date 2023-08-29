def numero_perfecto(a):
   n=1
   l=[]
   while n<a:
     if a%n==0:
       l.append(n)
     n=n+1
   m=0
   suma=0
   while m<len(l):
     suma=suma+l[m]
     m+=1
   if suma==a: 
     return True
   else:
     return False
     
           