# por favor escribe aquí tu función
def es_primo(num):
    if num<2:
       return False  
    for numm in range(2,num):
       if num % numm ==0:
          return False
       return True
           