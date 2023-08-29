import random

palabras=['cúspide','embelezo','moza','índigo','exótica','frenético','hiperbólica','sílfide','prolegómeno','lírica','marmóreo','sarcasmo','cuadrúmano','cacofonía','eufonía','anacrónico','paralítico','estrambótico','brígido','trémula','recóndito','pantruca','hostigar','alforja','carcaj','mimbrero','alcayota','pilcha','guaipe','monaguillo','mariscar','chumacera','érase','endomingado','hado','coquetuela','desengaño','ventisquero','atajo','orilla','holla','cumbrereño','taiga','tundra','estepa','arriero','ajeno','cuatrero','lancha','faena','navegar','minga','casamiento','hilandera','chamanto','fatiga','malograr','curanto','chapalele','milcao','ensenada','satisfecho','huija','persignar','escarcha','peonada','ovejero','patrón','lobería','antepasado','mísero','panteonero','amparo','genealógico','patrona','pampa','nortina','rosal','manda','reina','peregrino','tamarugal','tirana','contemplar','ranchera','tonada','sureña','patagonia','melodía','cascadas','tonada','pionero','firmamento']
vocales=['á','é','í','ó','ú']
tildes={'a':'á','e':'é','i':'í','o':'ó','u':'ú'}


def ocultar_letras(palabra,cantidad):
    palabrilla=list(palabra)
    indexes=[]
    j=0
    while j < cantidad:
        index=random.randint(0,len(palabra)-1)
        if index not in indexes:
            indexes.append(index)
            j+=1
    for i in indexes:
        palabrilla[i]='_'
    palabrilla="".join(palabrilla) 
    return palabrilla

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    if letra in palabra_secreta or (letra in vocales and tildes[letra] in palabra_secreta):
        for i in range(len(palabra_secreta)):
            if letra==palabra_secreta[i] and palabra[i]=='_':
                palabra[i]=palabra_secreta[i]
    palabra_secreta="".join(palabra_secreta)
    palabra="".join(palabra)
    return palabra

index=random.randint(0,len(palabras)-1)
parola=palabras[index]
ocultar=random.randint(1,len(parola))
mot=ocultar_letras(parola,ocultar)

if __name__ == "__main__":
    print(mot)
    mostrar=True
    intento=1
    while intento <=7 and mot!=parola:
        adivinanza=input("Intenta adivinar: ")
        if len(adivinanza)==1:
            mot_previa=mot
            mot=revisar_letra(parola,mot,adivinanza)
            if mot==mot_previa:
                print("La letra {0} no está en la palabra que estoy pensando".format(adivinanza))
            elif mot!=parola:
                print("¡Has advinado una letra!")
                print("{0} es lo que llevas de la palabra en que pienso".format(mot))
        elif adivinanza==parola:
            print("¡Has adivinado la palabra {0}!".format(parola))
            mostrar=False
            break
        else:
            print("Esa no es la palabra en que estoy pensando")
        intento+=1
    if mostrar==True and mot==parola:
        print("¡Has adivinado la palabra {0}!".format(parola))
    elif mostrar==True and mot!=parola:
        print("No has logrado adivinar la palabra {0}".format(parola))
         