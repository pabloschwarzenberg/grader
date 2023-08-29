def primo(x):
  lista=[]
  if x==2:
    return [2]
  else:
    i=2
    while i<x:
      if x%i==0:
        lista.append(i)
      else:
        i=i+1
    return lista



    
  
  
  
      