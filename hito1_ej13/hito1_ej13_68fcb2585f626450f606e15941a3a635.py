#Factores Primos
x=int(input("INGRESE UN NUMERO"))
def es_primo(num):
    if num < 2:    
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primos(num1, num2):
    for i in range(num1, num2):
        if es_primo(i) == True:
            if x%i==0:
                print (i)
print (primos(0, x))