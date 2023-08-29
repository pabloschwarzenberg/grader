import math


def suma_divisores(a):
    divisores = [i for i in range(1, a + 1) if a % i == 0]

    return sum(divisores)

def es_primo(x):
    if (x<=1):
        return False
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if(x%i==0 and i!=x):
            return False
    return True

if __name__ == "__main__":
    while True:
        try:
            efe = int(input("ingrese un numero: "))
            print(suma_divisores(efe))
            if es_primo(suma_divisores(efe)):
                print("Es primo")
            else:
                print("No es primo")
        except:
            print("incorrecto")