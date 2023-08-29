import sys
from random import randint     # Funciona Bien Pero Falta resolver ERROR 'str' object does not support item assignment 
ListaPalabras = ["columpio", "herramienta", "conserje", "guinda", "peyorativo ", "misantropia", "licantropia", "hipofisis", "hipotalamo", "ventriculo", "esclerosis", "necrosis", "isquemia", "filantropia", "epilepsia"]
palabra = ListaPalabras[randint(0,14)]
#word = palabra
palabra_l = list(palabra)
palabra_secreta = palabra

def ocultar_letras(palabra,cantidad):
    for i in range(cantidad):
        i = randint(0, len(palabra_l)-1)
        while palabra_l[i]== "_":
            i = randint(0, len(palabra_l)-1)
        palabra_l[i] = "_"
    palabra = palabra_l
    return palabra 


def revisar_letra(palabra_secreta,palabra,letra):
    secret_word = list(palabra_secreta)
    palabra_l = list(palabra)
    c = 0
    d = secret_word.count(letra)
    while c<d:
        x = secret_word.index(letra)
        if x >= 0:
            palabra_l[x + c] = letra
            secret_word.remove(letra)
        c += 1
    stri=""
    for i in range(0, len(palabra)):
            stri += palabra_l[i]
            palabra = stri
    return palabra




if __name__ == "__main__":
    print("")
    print("")
    print("   Debes adivinar la palabra secreta, puedes arriesgarte a decir la palabra completa,")
    print("   pero si te equivocas perderás automáticamente, o puedes intentar con 7 letras,")
    print("   una vez dicha tus 7 letras deberás decir la palabra completa.")

    
    ocultar_letras(palabra, len(palabra)-2)
    intentos = 0
    while intentos<7:
        print("")
        print("")
        print("   ", palabra_l)
        print("")
        opcion = input("  ¿Deseas intentar con una letra (1) o arriesgarte con la palabra completa (2)?:  ")
        while opcion != "1" and opcion != "2":
            opcion = input("  ¿Deseas intentar con una letra (1) o arriesgarte con la palabra completa (2)?:  ")
        if opcion == "1":
            letra = input("  ¿Que letra deseas comprobar?: ")
            revisar_letra(palabra_secreta, palabra, letra)
            print("  La palabra secreta ha quedado asi:")
            intentos += 1
        elif opcion == "2":
            respuesta = input("  ¿Cúal es la palabra secreta?: ")
            if respuesta == palabra_secreta:
                print("  La palabra secreta era:", palabra_secreta)
                print(" ¡Felicitaciones, has ganado!")
                sys.exit(1)
            else:
                print("  La palabra secreta era:", palabra_secreta)           
                print(" Lo lamento, has perdido.")
                sys.exit(2)
    print("   ", palabra_l)
    print("")
    print("")
    print("  Se te acabaron los intentos, debes arriesgarte.")
    respuesta = input("  ¿Cúal es la palabra secreta?: ")
    if respuesta == palabra_secreta:
        print("  La palabra secreta era:", palabra_secreta)
        print(" ¡Felicitaciones, has ganado!")
        sys.exit(1)
    else:
        print("  La palabra secreta era:", palabra_secreta)           
        print(" Lo lamento, has perdido.")
        sys.exit(2)