#Factores Primos
num = int(input("Número: "))
n=2
while n<=num:
    if num%n==0:
        print(n)
        num = num/n
    else:
        n+=1