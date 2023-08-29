def ocultar_letras(palabra,cantidad):
    if len(palabra) == 10 :
        palabra_secreta = 'lepidoptero'
        vidas = 7
    else:
        print('error')
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    while True:
        letra = input('')
        if vidas == 0:
            print ('no teni vida')
            break
        elif letra.lower() in palabra_secreta :
            print('Buena ql')
            break
        else:
            vidas = vidas-1
            print (' aweonaito')
            break
    return palabra

if __name__ == "__main__":
    palabra = input('Ingrese su palabra: ')
    x = ocultar_letras(palabra,cantidad)
    y = revisar_letra(palabra_secreta,palabra,letra)
    print('',x)
    print('',y)
    pass