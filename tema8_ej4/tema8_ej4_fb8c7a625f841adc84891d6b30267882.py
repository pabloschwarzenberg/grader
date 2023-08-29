def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    text_cifrado = ""
    for letra in palabra:
        print(abc.find(letra))
        suma =abc.find(letra) + 13
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
        
    return text_cifrado

 
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)