def numero_perfecto(a):

  Suma= 0

  for i in range(1, a-1):

    Resto= a%i
    
    if Resto == 0:
    
      Suma += i
    
  if Suma == a:
    
    numperf = 1
    
  else:
  
    numperf = 0
    
  return numperf
      
  
      
   
