#Factores Primos
def es_Primo(numero):
  esPrimo = True
  if numero ==1:
     esPrimo= False
  else:
   for x in range(2,numero-1):
     if numero % x ==0:
       esPrimo =False
         break
        
       return esPrimo