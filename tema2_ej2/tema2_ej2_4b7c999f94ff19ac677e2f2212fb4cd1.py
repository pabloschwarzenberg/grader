def suma_divisores(n):
    divisores = [1]
    
    
    
    for i in range(2, n + 1):
        if n % i == 0:
            divisores.append(i)
            
            return sum(divisores)
                  
     
     
        resultado = suma_divisores(12) # 1 + 2 + 3 + 4 + 6 + 12 = 28 
        print("resultado")
        resultado = suma_divisores(13) # 1 + 13 = 14
        print("resultado")
        resultado = suma_divisores(20) # 1 + 2 + 4 + 5 + 10 + 20 = 42
        resultado = suma_divisores(13) # 1 + 29 = 30
     
     