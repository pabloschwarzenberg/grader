#Factores Primos
a=int(input("ingrese un numero "))
i=1
while i<a:
    if a%i == 0:
        b=a/i
        if b%2 != 0 or b==2 b%11 != 0 b%3 !=0:
            print(i)
    i+=1