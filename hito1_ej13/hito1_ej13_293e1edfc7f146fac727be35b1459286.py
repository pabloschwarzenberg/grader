#Factores Primos
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

num = int(input())
n = num
primos = []

while (n != 1):
    for primo in range(2,num+1):
        if es_primo(primo):
            if n % primo == 0:
                n = n / primo
                primos.append(primo)
                break
        else:
            continue

for i in primos:
    print(i)