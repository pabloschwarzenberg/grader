def numero_perfecto(a):
   i=1
   suma=0
   while i<a:
     if a%i==0:
       suma=suma+i
     i=i+1
   if suma==a:
     return True
   else:
     return False

           