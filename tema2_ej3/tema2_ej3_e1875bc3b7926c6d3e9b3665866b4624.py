def numero_perfecto(a):
  i=1
  j=0
  k=0
  lista_divisores=[]
  while i<a :
    if (a%i)==0 :
      lista_divisores.append(i)
      i= i + 1
    else :
      i = i +1
  while k < len(lista_divisores):
    j=j+lista_divisores[k]
    k=k+1
  if j==a :
    return (True)
  else :
    return (False)
  
  
  
    
 
           