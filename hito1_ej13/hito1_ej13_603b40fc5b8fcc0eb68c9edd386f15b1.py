#Factores Primos
def factores_primos(X):
    for y in range (2, X+1):
        while X % y == 0:
            X = X/y
            print(y)
            
X = eval(input("De un número cualquiera uwu: "))
print(factores_primos(X))