def rot13(palabra):
    diccionario="abcdefghijklmnopqrstuvwxyz"
    for letter in palabra:
            if letter==diccionario[i] and letter<diccionario[13]:
                letter== diccionario[i+13]
            elif letter==diccionario[i] and letter >diccionario[13]:
                letter == diccionario [i-13]
    return palabra
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           