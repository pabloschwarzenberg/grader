import random


def ocultar_letras(palabra,cantidad):
    if cantidad>len(palabra): ### Si se quieren tapar mas letras de las que tiene la palabra, tapa maximo las letras que tiene la palabra
        cantidad=len(palabra)
    palabra=str(palabra) ### Me aseguro que sea un string
    posicion_al_azar=[]
    num=0
    while num!=cantidad: ### Le pido que me entregue posiciones al azar segun la cantidad que le pido
        posicion=random.randrange(0,len(palabra),1) ### numero al azar entre 0 y largo de la palabra separados por 1
        if posicion not in posicion_al_azar: ### Para que no se repitan posiciones
            posicion_al_azar.append(posicion)
            num+=1
    palabra_final="" #esto va a entregar
    
    for letra in range(0,len(palabra)): ### Voy a ir posicion por posicion de la palabra
        if letra in posicion_al_azar: ### Si la posicion esta en la lista al azar, escribe "-"
            palabra_final+="_"
        else:
            palabra_final+=palabra[letra] ### si la posicion no esta en la lista al azar entonces escribe la letra que esta en esa posicion de la palabra
    return(palabra_final)
    
def palabra_al_azar():
    Palabras=["calabaza","auto","numero","arbol","escuela","dia","corazon","computador","paralelepipedo"]
    palabra=random.choice(Palabras) ### Elige palabra al azar de la lista
    return(palabra)

def revisar_letra(palabra,palabra_actual,letra):
    posiciones=[]
    cantidad_de_aciertos=0
    if len(letra)==1: ## Si intente escoger una letra nomas
        Palabra_final=""
        for e in range(0,len(palabra)):
            if palabra_actual[e]!="_": ### Si la posicion revisada ya es una letra descubierta
                Palabra_final+=palabra_actual[e]
            elif (palabra_actual[e]=="_" and palabra[e]==letra):# Si la posicion revisada no esta descubierta y le achuntaste con la letra
                    cantidad_de_aciertos+=1
                    Palabra_final+=letra
            else:### Si la posicion revisada no esta descubierta pero no le achuntaste
                Palabra_final+="_"
        print("acertaste {} letras nuevas \n".format(cantidad_de_aciertos))
        print(Palabra_final)
        print("\n")
        return(Palabra_final)
    elif len(letra)>1: ## Si intentaste adivinar la palabra
        if letra == palabra:
            print("Adivinaste la palabra \n")
            return(palabra)
        else:
            print("no adivinaste la palabra \n")
            return(palabra_actual)
     
def Adivina_Palabra():
    palabra=palabra_al_azar()### traigo una palabra al azar

    letras_tapadas=random.randint(1,len(palabra)) ### Numero al azar entre 1 y largo de la palabra

    palabra_inicial=ocultar_letras(palabra,letras_tapadas) ### Genero la palabra oculta usando la palabra al azar

    palabra_actual=palabra_inicial # Partes con la palabra generada

    intentos=7 ### Tengo 7 intentos para adivinar

    llevo=0 ### Si "llevo" llega a 7, pierdo

    print("La palabra es : {} \n".format(palabra_actual))

    while llevo!=intentos:

        eleccion=input("Ingresa una letra o adivina la palabra \n")
        if len(eleccion)==1: ## Si eligió una letra
            print("ingresaste una letra \n")
            palabra_actual=revisar_letra(palabra,palabra_actual,eleccion)
            
        elif len(eleccion)==len(palabra): ### Si intento adivinar la palabra
            print("intentaste adivinar la palabra \n")
            palabra_actual=revisar_letra(palabra,palabra_actual,eleccion)
        else:### si ingreso cualquier otra cosa
            print("ingresaste cualquier cosa...pierdes un intento \n")
        llevo+=1

        if palabra_actual==palabra:
            print("Ganaste!!")
            return()
        print("te quedan {} intentos".format(intentos-llevo))

    print("Te quedaste sin intentos...perdiste")       