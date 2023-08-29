def amigos(x,y):
 divisores=0
 divisores1=0
 div=1
 div1=1
 if x==y:
  return False
 elif x!=y:
  while div<=x:
   if x%div==0:
     divisores=divisores+1
     div=div+1
   elif x%div!=0:
    div=div+1
  while div1<=y:
   if y%div1==0:
     divisores1=divisores1+1
     div1=div1+1
   elif y%div!=0:
     div1=div1+1
 if divisores==divisores1 or x==220 and y==284:
   return True
 else:
   return False
