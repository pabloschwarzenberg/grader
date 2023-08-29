# completa el código de la función
def amigos(a,b):
   c = 1
   d = 1
   r = 0
   s = 0
   while d < a:
      if a%d==0: 
         r = r + d
         d = d+1
      else:
         d = d+1
   while c < b:
      if b%c==0: 
         s = s + c
         c = c+1
      else:
         c = c+1
   if b == r and a == s:
         return True 
   else:
         return False
      
         
       


            