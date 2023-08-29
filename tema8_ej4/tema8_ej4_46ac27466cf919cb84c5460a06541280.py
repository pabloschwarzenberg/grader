def rot13(palabra):
    ROT13 = 'abcdefghijklmnopqrstuvwxyz'
    letra = ''
    for i in range(0,len(palabra)):
        for x in range(0,len(ROT13)):
            if str(palabra[i]) == str(ROT13[x]):
                if x >= 13:
                    b = x - 13
                    letra += ROT13[b]
                else:
                    letra += ROT13[x+13]
    return letra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    pass
           