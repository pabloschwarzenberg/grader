import random
def ocultar_letras(palabra,cantidad):
    if len(palabra) < cantidad :
        return False
    largo_palabra = len(palabra)
    rango = list(range(largo_palabra))
    random.shuffle(rango)
    digitos = rango[0:int(cantidad)]
    palabra_1 = list(palabra)
    for letra in digitos :
        palabra_1.pop(letra)
        palabra_1.insert(letra,"_")
    palabra_oculta = ''.join(palabra_1)
    return palabra_oculta
def revisar_letra(palabra_secreta,palabra,letra) :
    rango = list(range(len(palabra_secreta)))
    palabra_lista = list(palabra)
    for numero in rango :
        if palabra[numero] == "_" and letra == palabra_secreta[numero] :
            palabra_lista.pop(numero)
            palabra_lista.insert(numero,letra)
    palabra_final = ''.join(palabra_lista)
    return palabra_final


         