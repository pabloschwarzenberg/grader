# completa el código de la función
def amigos(a,b):
  posibles_divisoresa=1
  posibles_divisoresb=1
  sum_divisoresa=0  
  sum_divisoresb=0  

  while posibles_divisoresa<a:
      if a%posibles_divisoresa==0:
          sum_divisoresa+=posibles_divisoresa
      posibles_divisoresa+=1     
  while posibles_divisoresb<b:    
      if b%posibles_divisoresb==0:
          sum_divisoresb+=posibles_divisoresb
      posibles_divisoresb+=1 
         

          
  if sum_divisoresa==b and sum_divisoresb==a:       
    return True
  else:
     return False
          
