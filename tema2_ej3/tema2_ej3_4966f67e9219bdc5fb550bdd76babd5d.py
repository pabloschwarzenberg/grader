def numero_perfecto(a):
    adic = 0

    for i in range(1, a):
        if (a % (i) == 0):
            adic = adic + i
    if a == adic:
       return True
    else:
       return False
            
           