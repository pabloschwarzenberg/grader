# completa el código de la función
def suma_divisores(a):
    divisor = []
    for i in range(1, a):
        if a % i == 0:
            divisor.append(i)
    divisores = sum(divisor)
    if divisores == 1:
        primo = True
    else:
        primo = False
    return(divisores, primo)
if __name__ == "__main__":
    suma_divisores(int(input()))
           