def buscarTodas(a,b):
  l=[]
  e=""
  for i in range (len(a)):
    if a[i]==b:
      l.append(i)
      
  for c in range (len(l)):
    if c==len(l)-1:
      e=e+str(l[c])
    else:
      e=e+str(l[c])+str(" ")
  return (e)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  
    


           