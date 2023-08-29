def decodificar(mensaje):
    lista_binario = list(mensaje)
    list_elevados = []
    final = []

    palabra = ''

    lista_binario.reverse()
    contador = 0

    for i in lista_binario:
        if i == '1':
            elevado = 2 ** contador
            contador += 1
            list_elevados.append(elevado)
        elif i == '0':
            contador += 1
        if i == ',':
            contador = 0
            final.append(sum(list_elevados))
            list_elevados = []

    final.append(sum(list_elevados))
    final.reverse()

    for i in final:
        letra = chr(i)
        palabra = palabra + letra
    return palabra
         