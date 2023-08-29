def numero_perfecto(a):
    m = 0
    divisor = 1
    while divisor < a :
        if a % divisor == 0 :
            m += divisor
        divisor = divisor + 1
    if m == a :
      return True
    else :
      return False
           