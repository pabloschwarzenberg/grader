#Factores Primos
def es_primo(numero):
    if numero < 2:
        return False
    for a in range(2, numero):
        if numero % a == 0:
            return False
    return True

c = int(input())
for m in range(2, c):
    if es_primo(m) and c % m == 0:
        print(m)

if c == 2 or es_primo(c):
    print(c)

 
      