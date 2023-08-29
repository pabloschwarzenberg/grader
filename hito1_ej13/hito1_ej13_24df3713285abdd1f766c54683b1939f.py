#Factores Primos
factores = []
def Factores(a):
    for i in range(1, a + 1):
        if a % i ==0:
            Primo(i)
def Primo(numero):
    if numero !=1:
        for n in range(2, numero):
            if numero%n==0:
                return False
        factores.append(numero)
    else:
        return False

a=int(input("Ingrese un numero entero: "))         
Factores(a)
for x in range(len(factores)):
    print(factores[x])      