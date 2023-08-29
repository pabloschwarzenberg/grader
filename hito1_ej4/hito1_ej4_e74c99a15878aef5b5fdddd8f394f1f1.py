n=int(input("Número:"))
r=0
i=0
while n>0:
  a=n%2
  r=r+a*(10**i)
  i=i+1
  n=(n-a)/2
print("resultado=",r)
