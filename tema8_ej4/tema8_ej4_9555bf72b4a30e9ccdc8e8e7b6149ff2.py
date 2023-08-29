def rot13(palabra):
    prot13=""
    for i in range(len(palabra)):
        if 96<ord(palabra[i])<110:
            prot13+=chr(ord(palabra[i])+13)
        elif 109<ord(palabra[i])<123:
            prot13+=chr(ord(palabra[i])-13)
        else:
            return False   
    return prot13

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           