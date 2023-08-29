def es_primo(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
n = int(input("Ingrese un numero: "))
factores = []
facts = 2
while n > 1:
    if es_primo(facts):
        div = n % facts
        if div == 0:
            n = n // facts
            factores.append(facts)
        else:
            facts += 1
    else:
        facts += 1

for i in factores:
    print(i)