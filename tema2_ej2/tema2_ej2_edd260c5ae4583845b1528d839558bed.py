# completa el código de la función
def amigos(a,b):
  if suma_divisores(a)==b and suma_divisores(b)==a:
    return True
  else:
    return False
    
def suma_divisores(numero):
    suma=0
    for a in range (1, numero):
        if numero % a==0:
            suma+=a
    return suma  
          
           