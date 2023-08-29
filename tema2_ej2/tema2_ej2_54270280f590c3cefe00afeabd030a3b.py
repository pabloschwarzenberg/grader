# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    for i in range(1, a):
        if a%i == 0:
            suma1 = suma1 + i
        else:
            suma1 = suma1 + 0
    for j in range(1, b):
        if b%j == 0:
            suma2 = suma2 + j
        else:
            suma2 = suma2 + 0
            
    

    if suma1 == b and suma2 == a:
        return True
    else:
        return False


a = 220
b = 284
  
           

    
            
    
            

    
