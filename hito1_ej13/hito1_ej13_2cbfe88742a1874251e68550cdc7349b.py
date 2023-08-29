#Factores Primos
numero=int(input("Número: "))
while numero!=1:
    for i in range(2,numero+1):
        if numero%i==0:
            divisores=0
            for j in range(1,i):
                if i%j==0:
                    divisores=divisores+1
            if divisores==1:
                numero=round(numero/i)
                print(i)
                break   