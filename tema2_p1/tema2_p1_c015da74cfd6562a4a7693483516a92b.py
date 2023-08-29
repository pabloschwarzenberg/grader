# por favor escribe aquí tu función
def es_primo(numero):
    cont=0
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in lista:
        if numero%i==0 and numero%numero==0:
            cont+=1

            if cont==2:
                esPrimo=True

            else:
                esPrimo=False

    return esPrimo
           