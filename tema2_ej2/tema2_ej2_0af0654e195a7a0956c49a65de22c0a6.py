# completa el código de la función
def amigos(a,b):
    numero = a
    numero2 = b 
    divisor = 0
    total1 = 0
    total2 = 0
    if numero % 2 == 0:
        iterar = numero / 2
    else:
        iterar = (numero - 1) / 2

    for i in range(1, int(iterar) + 1):
        if numero % i == 0:
            aux = numero / i
            if aux != divisor:
                divisor = aux
            if i == iterar:
                print(int(divisor), end = "")
            else:
                total1 = int(total1 + divisor)

    if numero2 % 2 == 0:
        iterar = numero2 / 2
    else:
        iterar = (numero2 - 1) / 2

    for i in range(1, int(iterar) + 1):
        if numero2 % i == 0:
            aux = numero2 / i
            if aux != divisor:
                divisor = aux
            if i == iterar:
                print(int(divisor), end = "")
            else:
                total2 = int(total2 + divisor)

    total1 = total1 - numero + 1 
    total2 = total2 - numero2 + 1
    if total1 == numero2 and total2 == numero:
        retorno = True
    else:
        retorno = False
    return retorno
           