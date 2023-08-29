n=int(input("ingrese un numero primo"))
primo=[]
for i in range (2,n+1):
  while n%i==0:
    primo.append(i)
    n=n/i
for primo in primo:
  print(primo)