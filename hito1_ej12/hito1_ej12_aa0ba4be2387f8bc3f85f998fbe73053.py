#Juego adivina mi númeroimport random
import random
numse=random.randint(1,20)
fr=True
inte=1
while(fr==True):
    if((inte<=5)):
        numusu=int(input("ingrese un numero del 1 al 20 y pruebe su suerte"))
        if(numusu==numse):
            print("Adivinaste, mi número era",numse)
            fr=False
        elif(numusu<numse):
            print("el numero secreoto es mayor a ese")
            fr=True
            inte=inte+1
        elif(numusu>numse):
            print("el numero secreto es menor a ese")
            fr=True
            inte=inte+1
    else:
        print("No adivinaste, mi número era", numse)
        fr=False