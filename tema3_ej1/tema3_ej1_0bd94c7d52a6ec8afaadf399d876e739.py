# completa el código de la función
a = 1
def suma_divisores(a):
    if a == 1:
        divisores = []
        for i in range(2,a+1):
            if a % i == 0:
                if i != a:
                    divisores.append(i)
        numero = sum(divisores)
    else:
        divisores = [1]
        for i in range(2, a + 1):
            if a % i == 0:
                if i != a:
                    divisores.append(i)

        numero = sum(divisores)
    y = 2
    z = 3
    a = 5
    b = 7
    c = 11
    valor = ""
    if numero % y == 0:
        if numero == 0:
            valor = True
        elif numero / y != 1:
            valor = False
        else:
            valor = True
    elif numero == 1:
        valor = False

    elif numero % c == 0:
        if numero == 0:
            valor = True
        elif numero / c != 1:
            valor = False
        else:
            valor = True

    elif numero % z == 0:
        if numero == 0:
            valor = True
        elif numero / z != 1:
            valor = False
        else:
            valor = True

    elif numero % a == 0:
        if numero == 0:
            valor = True
        elif numero / a != 1:
            valor = False
        else:
            valor = True

    elif numero % b == 0:
        if numero == 0:
            valor = True
        elif numero / b != 1:
            valor = False
        else:
            valor = True
    elif numero == 0:
        valor = True
    return (numero,not valor)