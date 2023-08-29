#Factores Primos
num = int(input("Ingrese numero:"))
x=2
while (num!=1):
    if(num%x==0):
        print(x)
        num=num/x;
    else:
        x=x+1
              