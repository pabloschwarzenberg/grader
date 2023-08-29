import string
letras = string.ascii_lowercase
def rot13(palabra):
    clave=13
    text_cifrado=""
    for letra in palabra:
        suma=letras.find(letra)+clave
        modulo=int(suma)%len(letras)
        text_cifrado=text_cifrado+str(letras[modulo])
    return text_cifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           