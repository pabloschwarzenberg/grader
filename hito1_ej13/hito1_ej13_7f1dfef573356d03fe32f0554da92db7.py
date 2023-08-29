#Factores Primos
a = int(input())
divisor = 2
while divisor <= a :
    if a % divisor == 0 :
        print (divisor)
    divisor = divisor + 1 