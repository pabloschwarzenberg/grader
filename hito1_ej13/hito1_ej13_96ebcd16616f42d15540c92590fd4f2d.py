#Factores Primos

def es_primo(numero):
    numero = int(numero)
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


num = int(input())
frase = ""
lista = []
a= num


if num == 2:
    print("2")
else:
    for i in range(2, num):
        if es_primo(i) == True:
            if (a/i - int(a/i)) == 0:
                lista.append(i)

for x in lista:
    frase = frase + str(x) + "\n"


print(frase)