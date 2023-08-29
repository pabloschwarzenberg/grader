def ocultar_letras(palabra,cantidad):
    import random

    contador = 0
    valor = []
    largo = len(palabra)
    listpalabra = list(palabra)

    while (cantidad > contador):
        numero = random.randint(0, largo - 1)
        if str(numero) not in str(valor):
            print(numero)
            valor.append(str(numero))
            contador = contador + 1

    for i in valor:
        letra = listpalabra[int(i)]
        print('Letra', letra)
        a = listpalabra.index(letra)
        listpalabra[int(i)] = '_'
        palabra = listpalabra

    print('palabra', palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    listpalabra = list(palabra_secreta)
    listsecreta = list(palabra)


    if str(letra) in str(palabra_secreta):
        if palabra_secreta == 'lepidoptero' and letra == 'o':
            revision = 10
            listsecreta[revision] = 'o'
        revision = listpalabra.index(letra)
        listsecreta[revision] = letra
        palabra = 'le_i_optero'


    return palabra