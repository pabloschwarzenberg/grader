import math
def decimalabinario(numero, ls):
    if numero == 0:
        ls.reverse()
        numero = "".join([str(_) for _ in ls])
        print("resultado={}".format(numero))
    elif numero%2 ==1:
        ls.append(int(numero%2))
        decimalabinario(math.floor(numero/2), ls)
    elif numero%2 == 0:
        ls.append(int(numero % 2))
        decimalabinario(math.floor(numero / 2), ls)
numero = int(input("Ingrese numero decimal: "))
ls = []
decimalabinario(numero,ls)