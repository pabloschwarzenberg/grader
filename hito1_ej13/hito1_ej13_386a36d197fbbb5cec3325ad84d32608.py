#Factores Primos
def soy_primo(n):
    c=True
    for i in range(2, n):
        if (n%i==0):
            c=False
    return c
    
def primos(n):
    for j in range(2, n):
        if soy_primo(j)==True:
            while(n%j==0):
                print(j)
                n=n/j

n=int(input("Ingrese numero: "))
print(primos(n))
