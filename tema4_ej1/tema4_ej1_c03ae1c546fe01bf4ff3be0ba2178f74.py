import random
def ocultar_letras(palabra, cantidad):
    global palabra_secreta
    global k
    palabra_secreta=palabra
    k = random.choice(palabra_secreta)
    palabra_secreta = list(palabra)
    for i in range(0, cantidad):
        if k != "_":
            k = "_"
            palabra_secreta[i] = k
    return ("".join(palabra_secreta))


def revisar_letra(palabra_secreta, palabra, letra):
    if Decision.upper == "R":
        GUESS= input("WRITE YOUR GUESS: ")
        if GUESS == (PAL):
            print("YOU WIN")
    if Decision.upper == "T":
        while LIVES>0:
            for k in range(0,len(PAL)+1):
                if "T" == PAL[k]:
                    PALX[k] == "T"
                    print(PALX)
        if PALX==PAL_X:
            print("YOU LOSE ONE LIFE")
            LIVES-=1
            print("YOU HAVE ",LIVES,"LIFES")
        if PAL==PALX:
            print("YOU WIN")
        else:
            print(PALX)
    else:
        print("YOU DIED")
        LIVES=0
    return palabra
    
if __name__ == "__main__":
    pass
         