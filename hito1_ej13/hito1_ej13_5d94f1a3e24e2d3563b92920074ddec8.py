#Factores Primos
def factores_primos(n):
    divisores=0
    for a in range(2,n):
        if n%a==0:
           primer_divisor=a
           r=n/a
           for x in range(a,r):
               if r%x==0:
                  segundo_divisor=r
                  y=r/n
                  
                 
        else:
            return False
        
            
       
   