#Factores Primos
x=int(2)
a=int(input())
while a!=1:
    if a%x==0:
        print(str(x)+ " ");
        a=a/x;

    else:
        x=x+1     