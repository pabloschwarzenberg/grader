def rot13(palabra):
    num=13
    mensajecifrado=""
    for letra in palabra:
        z=ord("z")
        indice=ord(letra)+ num
        while indice>z:
            indice-=26
        mensajecifrado+=chr(indice)
    return mensajecifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           

           
