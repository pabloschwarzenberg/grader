#Factores Primos
n=int(input())
x=2
y=2
while x<n :
    if n%x==0 :
        print(x)
        x=x+1
    else:
        x=x+1