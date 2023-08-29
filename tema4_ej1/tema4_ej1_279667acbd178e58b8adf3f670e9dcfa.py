import random

def ocultar_letras(palabra,cantidad):
    lista_nueva = random.sample(range(0,len(palabra)), cantidad)
    for reemplazo in lista_nueva:
        palabra = palabra.replace(palabra[reemplazo], '_', 1)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    ls_plb_sc = list(palabra)
    if letra == palabra_secreta:
        return palabra_secreta
    for posicion,x in enumerate(palabra_secreta):
        #print(f'Posicion: {posicion}    x: {x}')
        if letra == x:
            ls_plb_sc[posicion] = letra
    palabra = ''.join(ls_plb_sc)
    return palabra

if __name__ == "__main__":
    pass
         