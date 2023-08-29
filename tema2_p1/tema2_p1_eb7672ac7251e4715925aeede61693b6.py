# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(num):
    if num==1:
        return False
    if num!=0:
         for divisor in range(2,num):
             resto=(num%divisor)
             if resto==0:
                 return False
             else: 
                return True
    
                               