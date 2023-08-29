#Factores Primos
num = int(input(" ingrese numero (mayor que 1)\n"))
x=2
while(num!=1):
    if(num%x==0):
        print(str(x)+"")
        num=num/x

    else:
        x=x+1