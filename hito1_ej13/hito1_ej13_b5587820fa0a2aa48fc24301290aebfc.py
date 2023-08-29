factor= []
def Factores(numero_primo):
    for i in range(1, numero_primo + 1):
        if numero_primo % i ==0:
            Primo(i)
def Primo(numeros):
    if numeros !=1:
        for n in range(2, numeros):
            if numeros%n==0:
                return False
        factor.append(numeros)
    else:
        return False

numero_entero=int(input("Ingrese un numero entero: "))         
Factores(numero_entero)
for x in range(len(factor)):
    print(factor[x])
