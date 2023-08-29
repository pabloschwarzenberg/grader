def amigos(x,y):
 suma1=1
 for xa in range(2,x):
  if(x%xa==0):
     suma1=suma1+xa
 suma2=1
 for ya in range(2,y):
  if(y%ya==0):
     suma2=suma2+ya
 if(suma1==y and suma2==x):
   return True
 else:
   return False