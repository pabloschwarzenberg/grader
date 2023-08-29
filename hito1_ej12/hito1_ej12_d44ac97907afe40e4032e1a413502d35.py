from random import randint

numAleatorio = randint(1,20)
cont = 0
pregunta = int(input("Adivina: "))
while pregunta != numAleatorio:

    cont +=1
    if cont == 5:
        print("No adivinaste, mi número era ", str(numAleatorio))
        break
    if int(pregunta) > numAleatorio:
        print("Oye enfermuto es menor el numero oe")
    elif int(pregunta) < numAleatorio:
        print("Oye enfurmto es mayor el numero O E")
    
    pregunta = input("iNgresa de nuevi oe")
if pregunta == numAleatorio:
    print("Adivinaste, mi número era ", str(numAleatorio))