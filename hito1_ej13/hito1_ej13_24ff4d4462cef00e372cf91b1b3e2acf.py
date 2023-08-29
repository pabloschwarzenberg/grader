def descomponer(numero):
    for feg in range(2, numero + 1):
        while numero % feg == 0:
            numero= numero/feg
            print(feg)

num=int(input("Por favor, inserte un Número: "))
print(descomponer(num))