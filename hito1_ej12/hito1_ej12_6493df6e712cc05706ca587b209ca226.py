#Juego adivina mi número
import random
numero = print(random.randint(10, 20))
oportunidad = 0
pregunta = ""

while oportunidad < 6:
    
    if pregunta == "":
        intento = int(input("elige un numero entre el 1 y el 20: "))
                
    if intento < numero:
        print("mi numero es menor")
        pregunta = ""
        oportunidad = oportunidad + 1
        
    
    elif intento > numero:
        print("mi numero es mayor")
        pregunta = ""
        oportunidad = oportunidad + 1
        
    elif intento == numero:
        print("Adivinaste, mi numero era",numero)
        break
if intento != numero:
numero = str(numero)
    print("no adivinaste, mi numero era",numero)    