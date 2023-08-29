def amigos(a,b):
    divisores = [1]
    for i in range(2,a + 1):   
      divisores1 = divisores.append(i)
      a2 = sum(divisores1)
    
    for i in range(2,b + 1):        
      divisores2 = divisores.append(i)
      b2 = sum(divisores2)    
   
    if a2 == b or b2 == a:
      return True
    
    else:
      return False