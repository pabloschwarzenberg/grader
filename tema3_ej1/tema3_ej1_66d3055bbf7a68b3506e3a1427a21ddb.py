def suma_divisores(numero):
    divisores=[0]
    
    for i in range(1,numero):
      
      if numero%i==0:
        divisores.append(i)
    
    x=sum(divisores)
    
    if sum(divisores)==1:
        return print(x,",",True)
    else:
        return print(x,",",False)
    
    
    

suma_divisores(13)
  