#Factores Primos
n=input()
nprim=[]
n=int(n)
i=1
while i< n:
  if i%n==0:
    nprim.extend([i])
    i+=1
  else:
    i+=1
for x in nprim:
  print(str(x))