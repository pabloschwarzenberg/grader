"""
Hito 2 ejercicio 4
@Autor: Manuel Solimano
22 Abril 2016
"""

import random
import sys

def ocultar_letras(palabra,cantidad):
    total = len(palabra)
    rd_list = []
    
    while len(rd_list) < cantidad:      #genera una lista con indices aleatorios no repetidos
        r = random.randint(0,total-1)
        if r not in rd_list:
            rd_list.append(r)
            
    out_str = ""
    
    for index in range(total):          #genera un nuevo str pero ocultando algunos caracteres          
        if index in rd_list:
            out_str += "_"
        else:
            out_str += palabra[index]
    return out_str

    
def revisar_letra(palabra_secreta,palabra,letra):
        
    out_str = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            out_str += letra
        else:
            out_str += palabra[i]
    return out_str


        

#------------------------------------------
if __name__ == "__main__":
    palabras = ["universidad","felino","programacion","python","trabajador","astronomia","penumbra"]

    while True:
        game = random.choice(palabras)
        cuantos = random.randint(1,len(game))
        ahorcado = ocultar_letras(game,cuantos)
        count = 0
        print("Bienvenido al juego del ahorcado, adivina la palabra, tienes 7 intentos: \n {}".format(ahorcado))
        while True:
            ing = input("Ingresa una letra, o adivina la palabra completa \n")
            count +=1
            
            if count > 7:
                print("Perdiste, la palabra secreta era ",game)
                sn = input("Quieres jugar de nuevo?(si/no) \n")
                if sn == "si":
                    break
                else:
                    print("Hasta luego!")
                    sys.exit(1)
                    
            if len(ing) > 1 and ing == game:
                print("Ganasste!, la palabra secreta era ",game)
                sn = input("Quieres jugar de nuevo?(si/no) \n")
                if sn == "si":
                    break
                else:
                    print("Hasta luego!")
                    sys.exit(1)
                    
            elif len(ing) > 1 and  ing != game:
                print("Incorrecto, esa no es la palabra secreta")
            else:
                ahorcado = revisar_letra(ahorcado,game,ing)
                if ahorcado == game:
                    print("Ganaste!, la palabra secreta era, ",game)
                    sn = input("Quieres jugar de nuevo?(si/no) \n")
                    if sn == "si":
                        break
                    else:
                        print("Hasta luego!")
                        sys.exit(1)
                else:
                    print("Adivina la palabra: \n {} \n".format(ahorcado))