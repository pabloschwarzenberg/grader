#Factores Primos
x=int(input('Ingresa un número : '))
a=2

for i in range (x):
    while x%a==0:
        print (a)
        x=x/a
        
    a=a+1      