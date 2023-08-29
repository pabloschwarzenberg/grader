import random

lista = ["peliculas","importante","vica","cultura","sociedad","generacion","musica"]
numero = random.randint(0,6)
pal = lista[numero]
intentos = 0
canti = random.randint(1,len(pal)-1)

def ocultar_letras(palabra,cantidad):
    palabraw = palabra
    while cantidad != 0 :
        randomn = random.randint(0,len(palabraw)-1)
        if palabraw[randomn] != "_":
            palabraw = palabraw[0:randomn] + "_" + palabraw[randomn+1:len(palabraw)]
            cantidad = cantidad - 1
    return palabraw

def revisar_letra(palabra_secreta,palabra,letra):
    global intentos
    for i in palabra_secreta:
        if i == letra:
            if palabra_secreta.find(i) == palabra.find(i):
                f = palabra_secreta.find(i,palabra_secreta.find(i)+1)
                palabra = palabra[0:f] + i + palabra[f+1:len(palabra)]
            else:
                f = palabra_secreta.find(i)
                palabra = palabra[0:f] + i + palabra[f+1:len(palabra)]
    intentos = intentos + 1
    
    return palabra

if __name__ == "__main__":

    a = ocultar_letras(pal,canti)
    print(a)
    while intentos <= 7:
        inten = str(input("Ingrese una letra o la palabra completa"))
        if inten == pal:
            print("Haz adivinado la palabra: era ",pal)
            break
        else:
            b = revisar_letra(pal,a,inten)
            print(b)
            a = b
            if b == pal:
                print("Haz adivinado la palabra: era ",pal)
                break
                
                                                              
    if intentos > 7:
        print("Haz perdido, la palabra era: ",pal)

