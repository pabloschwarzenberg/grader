#Factores Primos
def numeros(valor):
    for i in range(2, valor+1):
        while valor% i == 0:
            valor= valor/i
            print(i)
valor=int(input("ingrese un valor:"))
print(numeros(valor))      