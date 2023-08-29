#Factores Primos
numero = int(input("Ingrese numero: "))
num = list(str(numero))

if numero < 100:
    print(num[0]+'D',"+",num[1]+'U')

elif numero >= 100 and numero < 1000:
    print(num[0]+'C',"+",num[1]+'D',"+",num[2]+'U')

elif numero >= 1000 and numero <10000:
    print(num[0]+'M',"+",num[1]+'C',"+",num[2]+'D',"+",num[3]+'U')      