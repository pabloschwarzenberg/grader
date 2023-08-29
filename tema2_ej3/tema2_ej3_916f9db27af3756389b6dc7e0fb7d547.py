def numero_perfecto(a):
    suma_divisores = 0
    
    for i in range(1,a):
       if (a % (i) == 0):
          suma_divisores += (i)
          
    if a == suma_divisores:
    
       return True
       
    else:
       return False