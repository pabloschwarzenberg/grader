def rot13(texto):
    abcedario = "abcdefghijklmnopqrstuvwxyz"
    salida = ""
    for i in texto:
        salida += abcedario[(abcedario.find(i)+13)%26]
    return salida
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
           