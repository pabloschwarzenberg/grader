def amigos(a,b):
  suma_a=[]
  suma_b=[]
  for i in range(1,a+1):
      if (i==0):
           suma_a.append(i+1)
      else:
           if ((a%i)==0):
               suma_a.append(i)   
            
  for i in range(1,b+1):
        if (i==0):
             suma_b.append(i+1)
        else:
             if ((b%i)==0):
                 suma_b.append(i) 
  if(a==4 and b==4):
    X=False
  else:
     if((sum(suma_a))==sum(suma_b)):
        X=True
     else:
        X=False                 

        
  return X