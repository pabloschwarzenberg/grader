# completa el código de la función
import math

def suma_divisore(n):
    primos=0
    for i in range(1,n):
        if n % i ==0:
            primos+=1

    if primos < 2:
        return (n,False)
    else:
        return (n,True) 
if __name__ == "__main__":
    pass
           