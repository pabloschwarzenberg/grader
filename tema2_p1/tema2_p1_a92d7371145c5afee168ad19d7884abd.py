# por favor escribe aquí tu función
def es_primo(num):
      
  contador = 0
  if num==1:
    return False
  if num!=0:  
    for var1 in range(2,num):
        resto=num%var1
        if resto == 0:
            contador = contador+1
    if contador == 0:
      return True
    else:
      return False
