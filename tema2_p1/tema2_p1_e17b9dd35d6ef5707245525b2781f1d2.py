# por favor escribe aquí tu función
def es_primo(numero):
 while True: 
  if numero < 2:
    return False
  intento=2
  while intento<numero:
    if numero%intento==0:
       return False
    intento+=1
  return True

  
     
           