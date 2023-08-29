def jeringozo(string):
    resultado=" "
    for letra in string:
        if letra.lower() in "aeiou":
            resultado=resultado+letra+"p"+letra.lower()
        else:
            resultado=resultado+letra
    return resultado

if __name__=="__main__":
    string=input("Ingrese el texto:")
    texto_traducido=jeringozo(string) 
    print("Texto traducido a jeringozo:",texto_traducido)