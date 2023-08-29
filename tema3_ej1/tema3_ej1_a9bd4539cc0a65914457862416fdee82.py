# completa el código de la función
import math
def suma_divisores(a):
    divisores = [i for i in range(1, a + 1) if a % i==0]
    y = sum(divisores)
    for i in range(2, math.ceil(math.sqrt(y))+1):
        if(y%i==0 and i!=y):
            return y,False
    return y,True
#if __name__=="__main__":
    #x = int(input("ingrese un numero: "))
   # print(suma_divisores(x))