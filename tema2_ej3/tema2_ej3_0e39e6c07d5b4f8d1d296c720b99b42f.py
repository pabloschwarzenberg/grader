def numero_perfecto(a):
    b=0
    for n in range(1,a):
       if a%n==0:
          b=b+n
    if b==a:
       return True
    else:
        return False
  
           
   
            


           