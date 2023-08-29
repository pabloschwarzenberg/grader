# por favor escribe aquí tu función
def es_primo(numero):
    if numero==2 or numero==3 or numero==5: return True
    if numero%2==0 or numero<2: return False
    for divisor in range (2,numero): 
        if numero%divisor==0:              
              return False
    
    return True
  
    