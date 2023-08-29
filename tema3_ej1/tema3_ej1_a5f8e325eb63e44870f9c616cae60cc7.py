# completa el código de la función
import random
def suma_divisores(a):
    divisores=[1]

    for i in range(2,a+1):
        if a % i == 0:
            divisores.append(i)

    return sum(divisores)

a=random.randrange(1,100)
resultado=suma_divisores(a)
c=resultado-a
primo = c == 1
if __name__ == "__main__":
print(primo)