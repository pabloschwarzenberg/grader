# completa el código de la función
def suma_divisores(a):
 b=a-1
 d=0
 while b>0:
     if a%b==0:
         d+=b
         b-=1
     else:
         b-=1
 if d>1:
   return (d,False)
 elif d==0:
   return (d,False)
 else:
   return (d,True)
        
           