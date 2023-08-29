# completa el código de la función
def amigos(a,b):
    if a==2:
      return False
    if b==2:
      return False
    suma=0
    for i in range(1,a):
        if a%i == 0:
            suma=suma+i
            
    if suma==b:
        return True
    suma=0
    for i in range(1,b):
        if b%i == 0:
            suma=suma+i
    
    if suma==a:
        return True 
    
    else:
        return False  