#Factores Primos
n=int(input("n="))
d=2
b=2
c=0
while d<=n:
  div=n%d
  if div==0:
    while b<=d:
      if d%b==0:
        c=c+1
      b=b+1 
    if c==1:
      print(b-1)
      n=(n//(b-1))
    b=2
  c=0
  d=d+1

        
      