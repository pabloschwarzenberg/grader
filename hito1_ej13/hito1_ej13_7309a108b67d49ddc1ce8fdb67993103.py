#Factores Primos
a=int(2)
n=int(input("ingresa un numero:"))
while(n != 1):
  if(n%a==0):
    print(str(a)+"");n=n/a
  else:a=a+1
