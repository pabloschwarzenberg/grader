def numero_perfecto(a):
   
   f=0

   for i in range  (1,a):
       if a % i == 0:
           f += i
   if a == f:
       return True
   else:
       return False
