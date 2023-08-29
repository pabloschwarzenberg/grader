factores = []

def Es_Primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            continue
    return True

def Factores_Primos(num):
    for i in range(2,num):
        if num % i == 0:
            factores.append(i)
            continue
        else:
            pass   
    for n in factores:
        if Es_Primo(n) == True:
            continue
        else:
            factores.remove(n)
    return factores

numero = int(input("Ingrese numero: "))
print(Factores_Primos(numero))