import random


def ocultar_letras(palabra,cantidad):
    if cantidad>len(palabra):
        cantidad=len(palabra)
    palabra=str(palabra)
    posicion_al_azar=[]
    num=0
    while num!=cantidad:
        posicion=random.randrange(0,len(palabra),1)
        if posicion not in posicion_al_azar: 
            posicion_al_azar.append(posicion)
            num+=1
    palabra_final="" 
    
    for letra in range(0,len(palabra)): 
        if letra in posicion_al_azar:
            palabra_final+="_"
        else:
            palabra_final+=palabra[letra] 
    return(palabra_final)
    
def palabra_al_azar():
    Palabras=["calabaza","auto","numero","arbol","escuela","dia","corazon","computador","paralelepipedo"]
    palabra=random.choice(Palabras)
    return(palabra)

def revisar_letra(palabra,palabra_actual,letra):
    posiciones=[]
    cantidad_de_aciertos=0
    if len(letra)==1:
        Palabra_final=""
        for e in range(0,len(palabra)):
            if palabra_actual[e]!="_": 
                Palabra_final+=palabra_actual[e]
            elif (palabra_actual[e]=="_" and palabra[e]==letra):
                    cantidad_de_aciertos+=1
                    Palabra_final+=letra
            else:
                Palabra_final+="_"
        print("acertaste {} letras nuevas \n".format(cantidad_de_aciertos))
        print(Palabra_final)
        print("\n")
        return(Palabra_final)
    elif len(letra)>1:
        if letra == palabra:
            print("Adivinaste la palabra \n")
            return(palabra)
        else:
            print("no adivinaste la palabra \n")
            return(palabra_actual)
     
def Adivina_Palabra():
    palabra=palabra_al_azar()

    letras_tapadas=random.randint(1,len(palabra)) 

    palabra_inicial=ocultar_letras(palabra,letras_tapadas) 

    palabra_actual=palabra_inicial

    intentos=7 

    llevo=0 

    print("La palabra es : {} \n".format(palabra_actual))

    while llevo!=intentos:

        eleccion=input("Ingresa una letra o adivina la palabra \n")
        if len(eleccion)==1: 
            print("ingresaste una letra \n")
            palabra_actual=revisar_letra(palabra,palabra_actual,eleccion)
            
        elif len(eleccion)==len(palabra):
            print("intentaste adivinar la palabra \n")
            palabra_actual=revisar_letra(palabra,palabra_actual,eleccion)
        else:
            print("ingresaste cualquier cosa...pierdes un intento \n")
        llevo+=1

        if palabra_actual==palabra:
            print("Ganaste!!")
            return()
        print("te quedan {} intentos".format(intentos-llevo))

    print("Te quedaste sin intentos...perdiste")
