#Ordenar tres números
x=int(input())
x=str(x)
y=int(input())
y=str(y)
z=int(input())
z=str(z)
if x<=y<=z:
  print(x+","+y+","+z)
elif x<=z<=y: 
  print(x+","+z+","+y)
elif z<=x<=y:
  print(z+","+x+","+y)
elif z<=y<=x:
  print(z+","+y+","+x)
elif y<=x<=z:
  print(y+","+x+","+z)
elif y<=z<=x:
  print(y+","+z+","+x)