import random

tries = 0

print "Welcome to the word game!"
print "nI"m going to think of a word and you have to guess it!"
print "nGuess which letters are in the word, then you have to guess the whole thing!"
print "nGood luck!"

WORDS = ("follow", "waking", "insane", "chilly", "massive",
"ancient", "zebra", "logical", "never", "nice")

word = random.choice(WORDS)

correct = word
length = len(word)
length = str(length)

guess = raw_input("The word is " + length + " letters long. Guess a letter!: ")

while tries < 5:
for guess in word:
if guess not in word:
print "Sorry, try again."
else:
print "Good job! Guess another!"

tries = tries + 1 #*

if tries = 5:
final = raw_input ("Try to guess the word!: ")

if final = correct:
print "Amazing! My word was ", word, "!"

else:
print "Sorry. My word was ", word, ". Better luck next time!"

raw_input("nnPress enter to exit")

    intentos=0
    letras_almacenadas=[]
    i=0

    while True:

        if i==len(animal):
            print('-'*50)
            print('PERDISTE :( ... HASTA OTRA OPORTUNIDAD')
            print('-'*50)
            break

        if construir_palabra==word:
            print('-'*50)
            print('¡¡¡ G A N A S T E :) !!!')
            print('-'*50)
            break

        while True:
            letra=input('Ingresar letra: ')
            res=funcion_1(letra,letras_almacenadas) #Verifica si la letra ingresada no se repite
            if res==0:
                break
            print('**LETRA REPETIDA**')
            print()

        while True:
            vrf=funcion_2(letra,word,construir_palabra) #Verifica si la letra ingresada se encuentra en la palabra oculta

            if vrf==True:
                print('**Letra no encontrada: Intento N°'+str(intentos+1)+'**')
                print()
                intentos=intentos+1

                if intentos==3:
                    intentos=0
                    print(animal[i])
                    print()
                    i=i+1

                break
            else:
                construir_palabra=vrf
                print(construir_palabra)
                print()
                intentos=0
                break
       
         