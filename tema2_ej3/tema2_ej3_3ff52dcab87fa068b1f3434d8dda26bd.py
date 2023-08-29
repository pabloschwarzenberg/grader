def numero_perfecto(algo):
    sum=0
    for i in range(1,algo):
        if algo%i == 0:
            sum+=i
    if sum == algo:
        return True
    else:
        return False
        
        
        
        
        