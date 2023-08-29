#Factores Primos
def des_fac_primos(n):
    primos=[]
    for i in range(2,n+1):
        while n%i==0:
            primos.append(i)
            n=n/i
     print(primos)
    