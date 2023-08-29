# por favor escribe aquí tu función
def es_primo(numero):
    if (1<numero):

        divisor=2
        j=0

        while (divisor<numero):

            resto = numero%divisor

            if (resto==0):

                j+=1
            divisor+=1

        if (j==0):
             return True

        else:
            return False

    else:
        return False

try:
    n2 = int(input("Ingrese el numero al que desea saber si es primo o no: "))

    print (es_primo(n2))

except:

    print ("Solo proporcione numeros")        