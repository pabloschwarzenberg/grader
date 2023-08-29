def numero_perfecto(a):
    divisores=0
    for i in range(1,a):
        if a%i==0:
            divisores=divisores+i
    if divisores==a:
      return True
    else:
         return False