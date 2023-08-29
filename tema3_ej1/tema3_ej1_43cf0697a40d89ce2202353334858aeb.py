def suma_divisores(a):
    divisores = [0]
    for i in range (1,a):
         if a % i == 0:
             divisores.append(i)
    if   sum(divisores) == 1:
        x = True

    else:
        x = False

    return sum(divisores),x
if __name__ == "__main__":
    x = eval(input("Ingrese el numero"))
    print(suma_divisores(x))


