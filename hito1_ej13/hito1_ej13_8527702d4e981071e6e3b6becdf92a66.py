#Factores Primos
x=int(input( ))
n=2
divisores=[]
while n<=x:
    if x%n==0:
        x=x/n
        divisores.append(n)
        n=n+1
        
    elif x%n!=0:
        n=n+1
    elif x<n:
        break
for i in divisores:
    print(i)




  