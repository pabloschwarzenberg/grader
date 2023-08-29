def suma_divisores(a):
    var_Sumatoria = 0
    
    for indice in range(1, a - 1):
        var_Modulo = a % indice
        
        if var_Modulo != 0:
            continue
        
        var_Sumatoria += indice
    
    if var_Sumatoria == 1:
        var_NumPrimo = True
    else:
        var_NumPrimo = False
    
    return var_Sumatoria, var_NumPrimo