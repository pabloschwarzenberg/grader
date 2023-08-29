def jerigonzo(string):
    transcripcion = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            transcripcion  += letra
            transcripcion  += 'p'
        transcripcion  += letra
    return transcripcion 

if __name__ == "__main__":
    print(jerigonzo('frase'))
         