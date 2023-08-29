def suma_divisores(a): 
    sum = 0
    for i in range(1, a + 1): 
        sum += int(a / i) * i 
    return int(sum) 
      