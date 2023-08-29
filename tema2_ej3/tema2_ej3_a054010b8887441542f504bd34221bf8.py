def numero_perfecto(b):
#variable acalcular 
  fase=2
  div_numeros=0
  #suma de variable 
  agregar=1
  numero_perfecto= 0
  if b==1:
    numero_perfecto=0
    return(bool( numero_perfecto))
  while fase < b :
#division del numero   
      if b%fase == 0:
          agregar= agregar + fase    
      fase=fase + 1
  if agregar ==b:
      numero_perfecto=1
      return(bool( numero_perfecto))
  else:
      return(bool( numero_perfecto))
#si el numero es perfecto retorna      
           