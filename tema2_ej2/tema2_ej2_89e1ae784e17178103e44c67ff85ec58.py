# completa el código de la función
def amigos(a,b):
  sum_a=0
  sum_b=0
  for i in range(1,a):
      
     if a%i ==0:
      sum_a= sum_a+i
  
         
  for j in range(1,b):
      if b%j ==0:
       sum_b= sum_b+j
  
  if sum_a==b and sum_b==a:
      return True
  else:
      return False        