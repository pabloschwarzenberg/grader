#Factores Primos
x= int(2)
num=int(input("Ingrese numero:"))

while num !=1:
    if num % x ==0:
        print(x)
        num=num/x

    else:
        x = x+1
      