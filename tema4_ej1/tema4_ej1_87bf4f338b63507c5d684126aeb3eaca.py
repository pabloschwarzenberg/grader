# El juego consiste en tratar de adivinar una palabra secreta, dando algunas letras como pista.
# La persona tiene hasta 7 intentos para adivinar la palabra.

# Tu programa debe:

# Crear una lista con palabras secretas, y escoge aleatoriamente cuál palabra usarás para el juego.   (V)

# Escoger aleatoriamente cuántas letras mostrar de la palabra secreta, de acuerdo a la longitud de la
# palabra. Para ocultar las letras crea la función ocultar_letras(palabra, cantidad) que debe recibir
# como parámetro la palabra secreta y ocultar la cantidad de letras indicada, en posiciones
# aleatoriamente escogidas, reemplazándolas por “_”. Ej. ocultar_letras(“lepidoptero”,1)
# podría retornar “_epidoptero”, “lep_doptero”, “lepidopter_”, etc.

# El jugador debe poder ingresar una letra o arriesgarse a decir la palabra completa.
# Para revisar si una letra ingresada por el jugador existe en la palabra,
# crea la función revisar_letra(palabra_secreta, palabra, letra) que verifica si letra existe en la
# palabra secreta y la reemplaza en todas las posiciones que aparece en la palabra con las letras
# ocultadas, retornando la nueva palabra que debe mostrarse al jugador.
# Ej. revisar_letra(“lepidoptero”, ”lepidopter_”, ”o”) debería retornar lepidoptero.

# Importante: en este ejercicio solamente debes entregar funciones
# (que reciben los parámetros indicados en el ejercicio y que entregan su resultado con return),
# los input y los print para probar tu función los debes poner dentro de un
# if __name__ == "__main__": o quitarlos del programa al momento de subirlo a la plataforma.

#FUNCIONES Y RESULTADO CON RETURN
import random
palabras = ["cabeza","casa","calavera","burro","bandido","caballo","cabra"]
string = random.choice(palabras)
N1 = (string[0:1])
N2 = (string[1:2])
N3 = (string[2:3])
N4 = (string[3:4])
N5 = (string[4:5])
N6 = (string[5:6])
N7 = (string[6:7])
N8 = (string[7:8])
N9 = (string[9:10])
NT = (N1+N2+N3+N4+N5+N6+N7+N8+N9)
intentos = 0
##############################################
def leer_frase ():
    global txt
    txt=(NT)
def contar_letras():
    conta=0
    for i in txt:
        if(i.isalpha()):
         conta+=1
    print("contiene",conta,"letras")
leer_frase()
contar_letras()
#############################################
while intentos != 7:
    ingreso = input("ingrese palabra secreta: ")
    I1 = (ingreso[0:1])
    I2 = (ingreso[1:2])
    I3 = (ingreso[2:3])
    I4 = (ingreso[3:4])
    I5 = (ingreso[4:5])
    I6 = (ingreso[5:6])
    I7 = (ingreso[6:7])
    I8 = (ingreso[7:8])
    I9 = (ingreso[9:10])
    IT = (I1 + I2 + I3 + I4 + I5 + I6 + I7 + I8 + I9)
    print(IT)
    if IT == NT:
        print("Has acertado la palabra // Numero intentos =",intentos)
        intentos = intentos+1
        input("fin")
    elif I1 == N1:
        print(N1,"________")
        intentos = intentos + 1
    elif I2 == N2:
        print("_",N2,"________")
        intentos = intentos + 1
    elif I3 == N3:
        print("__",N3, "_______")
        intentos = intentos + 1
    elif I4 == N4:
        print("___",N4, "_____")
        intentos = intentos + 1
    elif I5 == N5:
        print("____",N5, "____")
        intentos = intentos + 1
    elif I6 == N6:
        print("_____",N6, "___")
        intentos = intentos + 1
    elif I7 == N7:
        print("______",N7, "__")
        intentos = intentos + 1
    elif I8 == N8:
        print("_______",N8,"_")
        intentos = intentos + 1
    elif I8 == N8:
        print("________",N9,)
        intentos = intentos + 1
else:
    print("se acabaron los intentos")
    input("fin")
