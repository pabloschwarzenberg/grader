#Factores Primos
     #5_Factores primos:
n=(input(""))
def descomponer(n):
    primos=[]
    for i in range((2,n+1)):
        while n%i==0:
            primos.append(i)
            n=n/i
    return primos

print(descomponer(n))