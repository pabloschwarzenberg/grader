import random

def ocultar_letras(palabra,cantidad):
    palabra_original = palabra
    palabra = list(palabra)
    i = 1
    while i <= cantidad:
        pos_letra = random.choice(range(0, len(palabra)))
        letra = palabra[pos_letra]
        if letra != '_':
            palabra[pos_letra] = '_'
            i += 1
        else:
            pass
    print("Palabra con _: ", ''.join(palabra))
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    palabra_secreta = list(palabra_secreta)
    i = 0
    while i < len(palabra):
        if letra == palabra_secreta[i]:
            palabra[i] = letra
        i += 1
    print(''.join(palabra))
    return ''.join(palabra)

if __name__ == "__main__":
    palabras = ["paralelepipedo", "jerigonza", "python", "lenguaje", "programacion", "lepidoptero"]
    palabra_elegida = random.choice(palabras)
    print("Palabra elegida:", palabra_elegida)
    cant_reemp = random.choice(range(1,len(palabra_elegida)+1))
    print("Cantidad de letras a reemplazar:", cant_reemp)
    palabra_ = ocultar_letras(palabra_elegida,cant_reemp)
    c = 1
    while c <= 7:
        letra_ing = input("Ingrese letra: ")
        palabra_ = revisar_letra(palabra_elegida,palabra_,letra_ing)
        if palabra_elegida == palabra_:
            print("Ganaste")
            break
        c += 1 