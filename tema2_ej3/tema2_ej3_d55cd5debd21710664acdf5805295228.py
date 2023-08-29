def numero_perfecto(valor):

    total = 0
    
    list = []
    
    for num in range(1, valor):
        
        if (valor%num == 0):
            
             list.append(num)
            
    for num in list:
        
        total += num
        
    if (total == valor):
        
        return True
    
    else:
        
        return False