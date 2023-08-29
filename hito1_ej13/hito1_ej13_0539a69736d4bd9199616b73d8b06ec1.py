#Factores Primos
def descomponer_factores(numero):
    x = 2
    while x <= numero:
        if not (numero % x != 0):
            print(x)
            numero /= x
        else:
            x += 1
a = int(input("numero : "))
print (descomponer_factores(a))