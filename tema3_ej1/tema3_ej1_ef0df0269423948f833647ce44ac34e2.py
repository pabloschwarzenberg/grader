# completa el código de la función
def suma_divisores(a):
    numero = a
    suma = 0
    es_primo = True

    while (numero > 0):
        if(a%numero == 0):
            if numero != a:
                suma=suma+numero
        numero = numero-1

    x = a 
    while (x > 0):
        if (a%x == 0):
            if x != a and x != 1:
                es_primo = False
        x = x - 1

    if suma == 1: es_primo = True
    if suma == 0: es_primo = False



    return (suma, es_primo)

           