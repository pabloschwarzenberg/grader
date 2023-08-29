# completa el código de la función
def amigos(a,b):
  divi=1
  divisores=[]
  while divi < a:
     if a % divi == 0:
         divisores.append(divi)
     divi +=1   
  sumadecosas=sum(divisores)
  if sumadecosas == b:
      valor = True
  else:
       valor= False
   
    
  return valor
           
           
  
  
