# completa el código de la función
def suma_divisores(numero):
    divs = [1]
    for r in range(2, numero+1):
        if numero % r == 0:

            divs.append(r)
    h = sum(divs)

    total = h - numero

    print(total)
    if total == 1:

        return total,True
    else:
        return total,False

if __name__ == "__main__":

    q = int(input("Ingrese un numero para recibir el calculo de la suma de sus divisores : "))
    result = suma_divisores(q)
    print(result)
