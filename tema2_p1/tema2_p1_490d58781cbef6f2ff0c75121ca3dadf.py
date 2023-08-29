def es_primo(x):
   i=2
   a=0
   if x==1:
     return False
   while i<x:
       if x%i==0:
           a=1
           return False
           break
       i=i+1
   if a!=1:
        return True
res=es_primo(4)
print(res)

           