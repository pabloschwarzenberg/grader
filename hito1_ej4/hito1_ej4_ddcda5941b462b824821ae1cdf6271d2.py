#Conversión de Decimal a Binario
import math
def decimalabinario(n, ls):
    if n == 0:
        ls.reverse()
        n = "".join([str(_) for _ in ls])
        print("resultado={}".format(n))
    elif n%2 ==1:
        ls.append(int(n%2))
        decimalabinario(math.floor(n/2), ls)
    elif n%2 == 0:
        ls.append(int(n % 2))
        decimalabinario(math.floor(n / 2), ls)
n = int(input("Ingrese numero decimal: "))
ls = []
decimalabinario(n,ls)