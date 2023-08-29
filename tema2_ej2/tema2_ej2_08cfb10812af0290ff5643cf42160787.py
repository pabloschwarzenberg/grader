def amigos(a,b):
    suma1 = 0
    suma2 = 0
    contador1 = 1
    contador2 = 1
    while True:
        if contador1 > a:
            break
        else:
            if a%contador1 == 0:
                
                suma1 += contador1
        contador1 = contador1 + 1
        
    while True:
        
        if contador2 > b:
            break
        else:
            
            if b%contador2 == 0:
                suma2 += contador2
              
        contador2 = contador2 + 1

    if suma1 == suma2 and a !=b:
        return True
    else:
        return False
           