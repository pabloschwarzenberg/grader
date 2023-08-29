def amigos(a,b):
 def suma(a):
     s=0
     for i in range(1,a):
         if a%i==0:
            s=s+i    
     return s
   
 if suma(a)==b and suma(b)==a:
     return True
 else:    
     return False