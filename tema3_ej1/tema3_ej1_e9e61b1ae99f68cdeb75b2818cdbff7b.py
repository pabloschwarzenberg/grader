def suma_divisores(a):
    if a==1 or a==0:
       return a-1,False 
    elif a == 2:
       return 1,True
    elif a > 2:
        for divisor in range(2,a):
          if a % divisor == 0:
             return a-1,False
          elif a % divisor != 0 and divisor == a-1:
             return 1,True
             