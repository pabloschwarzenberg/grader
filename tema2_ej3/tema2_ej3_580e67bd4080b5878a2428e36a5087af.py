def numero_perfecto(n):
    sum = 0
    divisor = n
    while divisor > 1:
        divisor = divisor - 1
        if (n % divisor) == 0:
            sum += divisor
    
    if(sum == n):
        return True
    else:
        return False
  