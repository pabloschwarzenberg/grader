# completa el código de la función
def amigos(a,b):
       global S
       S=0
       global D
       D=0
       for i in range(1,a):
              if(a % i==0):
                 S=S+i
        
       for m in range(1,b):
             if(b % m==0):
                 D=D+m
       if (S==b) and (D==a):
           return True
       else:
           return False
                
         

