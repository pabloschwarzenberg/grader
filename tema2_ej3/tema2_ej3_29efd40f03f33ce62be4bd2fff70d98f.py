def numero_perfecto(a):
   sum=0
   n=1
   while (n<a):
     if a%n==0:
       sum=sum+n
     n=n+1
   if (a==sum):
     return True
   else:
     return False
     
a= numero_perfecto(28)
print("Es perfecto?",a)

