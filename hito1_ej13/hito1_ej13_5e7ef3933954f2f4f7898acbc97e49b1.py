#Factores Primos
lis=[]
num= int(input("ingreseun numero entero:"))
i=2
while i<=num:
  if num%i==0:
    lis.append(i)
    num=num/i 
  else:
    i=i+1
for i in lis:
  print(i)