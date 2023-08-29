def rot13(palabra):
    Alfabeto = "abcdefghijklmnopqrstuvwxyz"
    FraseSalida = ""
    for i in palabra:
        FraseSalida += Alfabeto[(Alfabeto.find(i)+13)%26]
    return FraseSalida


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           