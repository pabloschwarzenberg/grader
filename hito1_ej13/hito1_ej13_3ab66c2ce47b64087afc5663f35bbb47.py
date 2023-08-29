L=int(input("INGRESE NAMBER"))
n=2
num_primo=[]
while n<=L:
  d=2 
  primo=True
  while d<n:
    if n%d==0:
      primo=False
      break
    d=d+1
  if primo and n>1:
    num_primo.append(n)
  n=n+1
for i in num_primo:
  print (i)