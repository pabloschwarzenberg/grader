def numero_perfecto(a):
  divisors = []
  for i in range(1,a):
    if (a % i)==0:
      divisors.append(i)
  suma = sum(divisors)
  
  if a == suma:
    return(True)
    
  else:
    return(False)
        
    
      


  
   












