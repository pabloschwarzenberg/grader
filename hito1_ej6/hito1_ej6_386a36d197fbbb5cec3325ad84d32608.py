x=int(input("numero 1:"))
y=int(input("numero 2:"))
z=int(input("numero 3:"))
if x<=y<=z:
 print(x,",",y,",",z)
 
elif x<=z<=y:
  print(x,",",z,",",y)
 
elif y<=z<=x:
  print(y,",",z,",",x)
  
elif y<=x<=z:
  print(y,",",x,",",z)
  
elif z<=x<=y:
  print(z,",",x,",",y)
 
elif z<=y<=x:
  print(z,",",y,",",x)

