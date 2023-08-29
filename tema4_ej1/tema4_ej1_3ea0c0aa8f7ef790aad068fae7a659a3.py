import random
stock=["perro","gato","rana"]

def ocultar_letras(palabra,cantidad):
    
    palabra=random.choice(stock)
    palabra=list(palabra)
    cantidad=len(palabra)
    palabra_secreta= ("_") * cantidad
    print (palabra_secreta)


def revisar_letra(palabra_secreta,palabra,letra):
    inicio= 0
    for letra in palabra:
        position= palabra.find(letra,inicio)
        palabra_secreta= palabra_secreta[:position] + letra + palabra_secreta [position + 1 :]
        inicio+=1

    return palabra_secreta



if __name__ == "__main__":
    run()