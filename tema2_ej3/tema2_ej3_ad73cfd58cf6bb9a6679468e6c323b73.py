def numero_perfecto(a):
    i=1
    acum=0
    while i<a:
        
        if a%i==0:
            acum=acum+i
        i=i+1
    if acum==a:
        return True
    else:
        return False
     
  