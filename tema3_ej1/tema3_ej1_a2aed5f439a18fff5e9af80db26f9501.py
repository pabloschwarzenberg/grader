# completa el código de la función
def suma_divisores(a):
    suma_div=0
    primo=True
    for i in range(1, a):
        if a%i==0:
            suma_div+=i
    if suma_div == 1:
        primo = True
    else:
        primo = False
    return (suma_div, primo)

if __name__ == "__main__":
    a=int(input())
    print(suma_divisores(a))