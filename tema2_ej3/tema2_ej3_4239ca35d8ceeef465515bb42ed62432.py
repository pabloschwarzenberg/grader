def numero_perfecto(a):
  suma=0
  for n in range(1,a):
    if a%n==0:
      suma+=n
  if suma==a:
    print("numero perfecto")
    return True
    
  return False  
 
       
 
  
        
      

  a=int(input("ingrese su numero:"))

  print(numero_perfecto(a))
           