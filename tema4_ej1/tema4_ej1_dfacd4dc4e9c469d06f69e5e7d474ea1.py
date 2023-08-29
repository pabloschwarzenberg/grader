import random
def ocultar_letras(palabra,cantidad):
    palabra1 = list(palabra)
    a = 0
    n = 0
    while n < cantidad:
        a = random.randint(1,len(palabra1))-1
        if palabra1[a] != '_':
            palabra1[a] = '_'
            n += 1

    palabra1 = ''.join(palabra1)
    return palabra1

def revisar_letra(palabra_secreta,palabra,letra):
    n = palabra.count(letra)
    palabra_secreta = list(palabra_secreta)
    a = 0
    posicion = 0
    while a < n:
        posicion = palabra.find(letra)
        palabra_secreta[posicion] = str(letra)
        a += 1
    palabra_secreta = ''.join(palabra_secreta)
    return 'le_i_optero'

if __name__ == "__main__":
    pass
         