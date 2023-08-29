#Contestador de celular
x=int(input())
y=int(input())
f=str(x)
g=str(x)
if y>=0 and y<7:
  print("CONTESTAR")
if y>=7 and y<14 and (f[-3:])!="909":
  print("NO CONTESTAR")
if y>=17 and y<19 and (g[0:3])!="877":
  print("CONTESTAR")
if y>=19:
  print("NO CONTESTAR")
else: 
  print("CONTESTAR")