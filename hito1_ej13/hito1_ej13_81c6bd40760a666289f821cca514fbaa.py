#Factores Primos
profe=int(input("ingresar numero: "))
n=2
while n<=profe:
    if profe%n==0:
        print(n)
        profe=profe/n
    else:
            n+=1