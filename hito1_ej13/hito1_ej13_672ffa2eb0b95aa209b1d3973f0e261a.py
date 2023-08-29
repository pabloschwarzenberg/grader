#Factores Primos
fprimo = int(input("Ingrese numero: "))
def descomponer1(numero):
    Nprimos = []
    for i in range(2, numero + 1):
        while numero % i == 0:
            Nprimos.append(i)
            numero = numero / i            
    for i in range(len(Nprimos)):
        print(Nprimos[i])
descomponer1(fprimo)