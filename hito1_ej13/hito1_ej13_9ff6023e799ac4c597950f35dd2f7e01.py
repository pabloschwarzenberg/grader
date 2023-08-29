#Factores Primos
n=int(input())
num=0
divisor=1
while divisor<n :
    if (n%divisor)==0:
        print(divisor)
        divisor = divisor+1
        num+=1
    else:
        divisor=divisor+1
      