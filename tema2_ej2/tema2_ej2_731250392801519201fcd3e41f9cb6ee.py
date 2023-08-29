# completa el código de la función
def amigos(a,b):
 def sumadiv(a):
     s=0
     for i in range(1,a):
         if a%i==0:
            s=s+i
     return s
 
 if sumadiv(a)==b and a==sumadiv(b):
    return True
 else:
      return False
     
     
     
     
     


  
           