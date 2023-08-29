numero = int(input("ingrese un numero: "))
primos = []
for i in range(2,numero+1):
    if numero%i==0:
        numero = numero/i
        print(i)