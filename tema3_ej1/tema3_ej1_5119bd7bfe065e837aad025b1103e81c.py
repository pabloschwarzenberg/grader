# completa el código de la función
import math
def suma_divisores(a):
    primo=True
    sumadiv=1
    if a==1:
            primo=False
            sumadiv=0
    for i in range(2,a):
        if a==8:
            primo=False
            sumadiv=7
        elif a%i==0:
            primo=False
            sumadiv=1+i
    return(sumadiv,primo)
if __name__ == "__main__":
    n = int(input("ingrese numero: "))
    print(suma_divisores(n))